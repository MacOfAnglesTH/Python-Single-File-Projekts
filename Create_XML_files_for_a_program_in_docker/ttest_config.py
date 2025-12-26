######################################################################################################
# This Python file generate a the configuration files for the ttest-application.
# The files have XML-Format and will be deployed in a docker container
# @author Mac Mueller
# Date: 19.12.2025
######################################################################################################
######################################################################################################

import xml.etree.ElementTree as XML
import socket
from xml.dom import minidom

ROOT = XML.Element('TTESTmeta')
ON = 'On'
OFF = 'Off'
PATH = 'C:\\python\\' #2be update later
SUTSERVICES = [ 'SBEPS', 'SDGP', 'SEBP', 'SEPS', 'SILSI', 'STVS' ]
HOSTNAME = socket.gethostname().upper()
EVO = 'sevo01' #2be update later

def comment(element):
	"""Create comment with XML element

	:ElementTree element: XML ElementTree Object
	:Str return: commended XML-Code
	"""
	commented = XML.Comment(XML.tostring(element, encoding='unicode'))
	return commented

def root_init():
	"""Set the XML-root for all document"""
	ROOT.set('xmlns', 'http://meta.TTEST.PRIVATEgroup.com')
	ROOT.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
	ROOT.set('xsi:schemaLocation', 'http://meta.TTEST.PRIVATEgroup.com TTESTmeta.xsd')

def write(name):
	"""Save the XML to a local-file with pretty-print, then empty the root-XML.

	:Str name: The name of file to save, the path was declear as constant
	"""
	root_init()
	dom = minidom.parseString(XML.tostring(ROOT, encoding='utf-8'))
	pretty_bytes = dom.toprettyxml(indent='  ', encoding='utf-8')
	with open(PATH + name, 'wb') as f: 
		f.write(pretty_bytes)
	ROOT.clear()

## AnalgeKonfiguration.xml
def write_sys_config():
	anlagen_configs = XML.SubElement(ROOT, 'AnlagenConfigs')
	anlagen_config = XML.SubElement(anlagen_configs, 'AnlagenConfig', Name='VV', ShortSign='VV', idNumber='169', GitRepo='VV')
	XML.SubElement(anlagen_config, 'ORESTOutput', Location='/elektra/ttest/bhf00/meta/dok/')
	XML.SubElement(anlagen_config, 'MetaExport', Location='/elektra/ttest/bhf00/meta/dok/', GitPath='/ttest/')
	anlagen_config.append(comment(XML.Element('EPPOutput', Location='/elektra/ttest/bhf00/meta/WT.xml', GitPath='/ttest/')))
	XML.SubElement(anlagen_config, 'TvsDataPrep', Location='/elektra/ttest/bhf00/meta/TVS.xml')
	SERVICES_STATUS = [ ON, ON, OFF, ON, ON, 'ohneRoby' ]
	for (service,status) in zip(SUTSERVICES, SERVICES_STATUS):
		XML.SubElement(anlagen_config, 'SUTservice', {service:status})
	write('AnalgeKonfiguration.xml')	

## BasisKonfiguration.xml
def write_basic_config():
	XML.SubElement(ROOT, 'GenericConfig',Location='/elektra/PRIVATE/bhf00/config/', Installation='InstallationsKonfiguration.xml', Labor='LabKonfiguration.xml', Anlagen='AnlageKonfiguration.xml')
	XML.SubElement(ROOT, 'Platform', Name=HOSTNAME, Machine=HOSTNAME)
	XML.SubElement(ROOT, 'GitBase', Location='/home/pri_vate/labgit/')
	application_config = XML.SubElement(ROOT, 'ApplicationConfig')
	XML.SubElement(application_config, 'application', Type='SBEPS', Location='/virt/tools/SEPS/SEPS_05.29/sbeps', Parameters='--system=[%EVO]SBB --station=[%STATION] --nostatuswind', prompt='e> ')
	XML.SubElement(application_config, 'application', Type='SEBP', Location='/virt/tools/SEPS/SEPS_05.29/sbpg_if.pl', Parameters='--system=[%EVO]SBB --init=sbb_[%STATIONLC].config')
	XML.SubElement(application_config, 'application', Type='SILSI', Location='/virt/tools/SILSI/SILSI_01.25.4/silsi', Parameters='--system=[%EVO]SBB --station=[%STATION] --appldir=/elektra/private/SBB/private/srcu --datadir=/tas/private/labor/VELCH/[%EVO]/appl/AEOS5-X86/DB/seps --sbeps=[%EVO]SBB')
	XML.SubElement(application_config, 'application', Type='srdu_read', Location='/tas/el_evolution/labor/tools/srdu_read', Parameters='[%EVO]-002 > /elektra/ttest/bhf00/log/SDGP.[%STATION].[%EVO].log')
	sut_service_config = XML.SubElement(ROOT, 'SUTserviceConfig')
	for service in SUTSERVICES:
		if service in ('SBEPS', 'SILSI', 'SEBP', 'SDGP', 'STVS'):
			sutService = XML.SubElement(sut_service_config, 'SUTservice', Type=service)
			if service != 'STVS':
				channel = XML.SubElement(sutService, 'channel', Type=service, application='SBEPS')
			if service == 'SBEPS':
				XML.SubElement(channel, 'execute', command='extend syt')
				XML.SubElement(channel, 'execute', command='attach seps')
			if service == 'SILSI':
				XML.SubElement(sutService, 'required', application=service)
				XML.SubElement(channel, 'execute', command='extend sbb_silsi.epl silsi')
				XML.SubElement(channel, 'execute', command='attach silsi')
			if service == 'SEBP':
				XML.SubElement(sutService, 'required', application=service)
				XML.SubElement(channel, 'execute', command='extend sbb_sebp')
				XML.SubElement(channel, 'execute', command='attach sebp')
				XML.SubElement(channel, 'execute', command='fapack off')
			if service == 'SDGP':
				XML.SubElement(sutService, 'required', application='srdu_read')
				del channel.attrib['application']
	autostart_options = XML.SubElement(ROOT, 'AutostartOptions')
	GITCOMMANDS = ['gitcommit', 'init sdlg', 'univ', 'init startup']
	for gitCommand in GITCOMMANDS:
		autostart_option = XML.Element('AutostartOption', Name=gitCommand, State='Off')
		if gitCommand in ('gitcommit', 'init startup'):
			autostart_options.append(autostart_option)
		else:
			autostart_options.append(comment(autostart_option))
	debug_options = XML.SubElement(ROOT, 'DebugOptions')
	DEBUGOPTIONSNAMES = ['SSH', 'STARTUPCOMPONENTS', 'SDGP', 'SDGP_FULL', 'SEBP', 'SSEPS', 'SILSI', 'SILSIBITS', 'GIT', 'SEVENTBUS', 'SSIGTAB', 'SSTARTUPCOMPONENTS', 'STRAIN_CMD']
	for option in DEBUGOPTIONSNAMES:
		debug_options.append(comment(XML.Element(option, State='on')))
	write('BasisKonfiguration.xml')

## InstallationsKonfiguration.xml
def write_install_config():
	install_config = XML.SubElement(ROOT, 'InstallationConfig', WebInterface='192.168.private.10:8091')
	testplatform = XML.SubElement(install_config, 'Testplatform', Name=socket.gethostname(), evo=EVO)
	XML.SubElement(testplatform, 'Asset', Name='VV')
	for service in SUTSERVICES:
		service_element = XML.Element('SUTservices')
		service_element.set(service, OFF)
		testplatform.append(service_element)
	write('InstallationsKonfiguration.xml')

## LabKonfiguration.xml
def write_lab_config():
	lab_config = XML.SubElement(ROOT, 'LabConfig')
	platform = XML.SubElement(lab_config, 'Platform', Name=HOSTNAME, Type='Container')
	XML.SubElement(platform, 'Webride')
	machine = XML.SubElement(platform, 'Machine', Hostname=HOSTNAME, IP='192.168.private.10', username='private', password='privatePass', bashprompt='private@' + HOSTNAME + '-bhf00-ve2:~$')
	for i in range(1, 10, 1):
		evo_number = str(i)
		installation = XML.SubElement(machine, 'Installation', evo='evo0' + evo_number, Net='192.168.' + evo_number + '.0', NetMask='255.255.255.0')
		for service in SUTSERVICES:
			if service == 'SEPS':
				XML.SubElement(installation, service, TVSPORT='192.168.private.10:3302'+evo_number)
			elif service == 'SILSI':
				XML.SubElement(installation, service, P1='192.168.private.10:3312'+evo_number, P2='192.168.private.10:3310'+evo_number)
			elif service == 'SDGP':
				XML.SubElement(installation, service, Datalogger='192.168.private.10:3300'+evo_number)
			elif service == 'STVS':
				XML.SubElement(installation, service, EPS='172.16.private.105:8497', Webride='172.16.private.207:3400'+evo_number)
			else:
				XML.SubElement(installation, service)
	write('LabKonfiguration.xml')

if __name__ == '__main__':
	write_sys_config()
	write_basic_config()
	write_install_config()
	write_lab_config()