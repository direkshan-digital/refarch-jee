Cell=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/')
Node=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/')
Server=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/Server:server1')
Server=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/Server:server1')
Node=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/')
Cell=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/')
NodeName=AdminControl.getNode()

print 'Starting Creating JVM Properties'
AdminTask.setJVMProperties(Server, ["-classpath", "{}" , "-maximumHeapSize", "0" , "-initialHeapSize", "0" , "-genericJvmArguments", "'-Xquickstart'" ])
AdminConfigVar_8=AdminConfig.list('JavaVirtualMachine', Server)
systemPropertiesAttr=[]
systemPropertiesAttr.append([['name', 'com.ibm.security.jgss.debug'], ['value', 'off']])
systemPropertiesAttr.append([['name', 'com.ibm.security.krb5.Krb5Debug'], ['value', 'off']])
systemPropertiesAttr.append([['name', 'com.ibm.ws.management.event.pull_notification_timeout'], ['value', '120000']])
AdminConfig.modify(AdminConfigVar_8, [['systemProperties', systemPropertiesAttr]])

print 'Starting Creating Authenication Alias'
GlobalSecurityVar=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/' + 'Security:/')
AdminConfig.create('JAASAuthData', GlobalSecurityVar, [['password', '{xor}Oz1tNjEsK25yLyg7'], ['userId', 'db2inst1'], ['alias', 'localhostNode01/DBUser'], ['description', '']])

print 'Starting Creating Connection Factories'

print 'Starting Creating JDBC Providers'
AdminConfigVar_11=AdminConfig.create('JDBCProvider', Cell, [['providerType', 'DB2 Using IBM JCC Driver (XA)'], ['name', 'DB2_Using_IBM_JCC_Driver_(XA)'], ['description', 'Two-phase commit DB2 JCC provider that supports JDBC 4.0 using the IBM Data Server Driver for JDBC and SQLJ. IBM Data Server Driver is the next generation of the DB2 Universal JCC driver. Data sources created under this provider support the use of XA to perform 2-phase commit processing. Use of JDBC driver type 2 on WebSphere Application Server for Z/OS is not supported for data sources created under this provider. This provider is configurable in version 7.0 and later nodes.'], ['implementationClassName', 'com.ibm.db2.jcc.DB2XADataSource'], ['classpath', '${DB2_JCC_DRIVER_PATH}/db2jcc4.jar;${UNIVERSAL_JDBC_DRIVER_PATH}/db2jcc_license_cu.jar;${DB2_JCC_DRIVER_PATH}/db2jcc_license_cisuz.jar'], ['xa', 'true']])
AdminConfigVar_12=AdminTask.createDatasource(AdminConfigVar_11, ["-name", "OrderDS" , "-jndiName", "jdbc/orderds" , "-dataStoreHelperClassName", "com.ibm.websphere.rsadapter.DB2UniversalDataStoreHelper" , "-componentManagedAuthenticationAlias", "localhostNode01/DBUser" , "-xaRecoveryAuthAlias", "localhostNode01/DBUser" , "-configureResourceProperties", "[[databaseName java.lang.String ORDERDB] [driverType java.lang.Integer 4] [serverName java.lang.String localhost] [portNumber java.lang.Integer 50000] ]" ])
AdminConfigVar_13=AdminConfig.showAttribute(AdminConfigVar_12, 'propertySet')
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'retrieveMessagesFromServerOnGetMessage'], ['value', 'true'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'beginTranForVendorAPIs'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'validateNewConnectionRetryCount'], ['value', '100'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'useTransactionRedirect'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'jmsOnePhaseOptimization'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'enableMultithreadedAccessDetection'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'reauthentication'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'connectionSharing'], ['value', '1'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'nonTransactionalDataSource'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'validateNewConnectionRetryInterval'], ['value', '3'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'name'], ['value', 'OrderDS'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'freeResourcesOnClose'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'traceLevel'], ['value', '-1'], ['type', 'java.lang.Integer']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'beginTranForResultSetScrollingAPIs'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'unbindClientRerouteListFromJndi'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'preTestSQLString'], ['value', 'SELECT CURRENT SQLID FROM SYSIBM.SYSDUMMY1'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'validateNewConnection'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_13, [['name', 'errorDetectionModel'], ['value', 'ExceptionMapping'], ['type', 'java.lang.String']])
AdminConfigVar_14=AdminConfig.showAttribute(AdminConfigVar_12, 'connectionPool')
AdminConfig.modify(AdminConfigVar_14, [['reapTime', '180'], ['surgeCreationInterval', '0'], ['surgeThreshold', '-1'], ['unusedTimeout', '1800'], ['purgePolicy', 'EntirePool'], ['testConnection', 'false'], ['numberOfSharedPoolPartitions', '0'], ['minConnections', '1'], ['stuckTimerTime', '0'], ['freePoolDistributionTableSize', '0'], ['numberOfUnsharedPoolPartitions', '0'], ['numberOfFreePoolPartitions', '0'], ['stuckTime', '0'], ['testConnectionInterval', '0'], ['connectionTimeout', '180'], ['agedTimeout', '0'], ['maxConnections', '10'], ['stuckThreshold', '0']])
AdminConfigVar_15=AdminTask.createDatasource(AdminConfigVar_11, ["-name", "INDS" , "-jndiName", "jdbc/inds" , "-dataStoreHelperClassName", "com.ibm.websphere.rsadapter.DB2UniversalDataStoreHelper" , "-componentManagedAuthenticationAlias", "localhostNode01/DBUser" , "-xaRecoveryAuthAlias", "localhostNode01/DBUser" , "-configureResourceProperties", "[[databaseName java.lang.String INDB] [driverType java.lang.Integer 4] [serverName java.lang.String localhost] [portNumber java.lang.Integer 50000] ]" ])
AdminConfigVar_16=AdminConfig.showAttribute(AdminConfigVar_15, 'propertySet')
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'retrieveMessagesFromServerOnGetMessage'], ['value', 'true'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'beginTranForVendorAPIs'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'validateNewConnectionRetryCount'], ['value', '100'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'useTransactionRedirect'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'jmsOnePhaseOptimization'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'enableMultithreadedAccessDetection'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'reauthentication'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'connectionSharing'], ['value', '1'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'nonTransactionalDataSource'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'validateNewConnectionRetryInterval'], ['value', '3'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'name'], ['value', 'INDS'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'freeResourcesOnClose'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'traceLevel'], ['value', '-1'], ['type', 'java.lang.Integer']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'beginTranForResultSetScrollingAPIs'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'unbindClientRerouteListFromJndi'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'preTestSQLString'], ['value', 'SELECT CURRENT SQLID FROM SYSIBM.SYSDUMMY1'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'validateNewConnection'], ['value', 'false'], ['type', 'java.lang.String']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_16, [['name', 'errorDetectionModel'], ['value', 'ExceptionMapping'], ['type', 'java.lang.String']])
AdminConfigVar_17=AdminConfig.showAttribute(AdminConfigVar_15, 'connectionPool')
AdminConfig.modify(AdminConfigVar_17, [['reapTime', '180'], ['surgeCreationInterval', '0'], ['surgeThreshold', '-1'], ['unusedTimeout', '1800'], ['purgePolicy', 'EntirePool'], ['testConnection', 'false'], ['numberOfSharedPoolPartitions', '0'], ['minConnections', '1'], ['stuckTimerTime', '0'], ['freePoolDistributionTableSize', '0'], ['numberOfUnsharedPoolPartitions', '0'], ['numberOfFreePoolPartitions', '0'], ['stuckTime', '0'], ['testConnectionInterval', '0'], ['connectionTimeout', '180'], ['agedTimeout', '0'], ['maxConnections', '10'], ['stuckThreshold', '0']])

print 'Starting Creating websphereVariables'
varSubstitutions =AdminConfig.list("VariableSubstitutionEntry",Cell).split(java.lang.System.getProperty("line.separator"))
for varSubst in varSubstitutions:
	getVarName = AdminConfig.showAttribute(varSubst, "symbolicName")
	if getVarName == "DB2_JCC_DRIVER_PATH":
		AdminConfig.modify(varSubst, [['value', '/opt/ibm/db2/V11.1/java']])
	if getVarName == "DERBY_JDBC_DRIVER_PATH":
		AdminConfig.modify(varSubst, [['value', '${WAS_INSTALL_ROOT}/derby/lib']])
	if getVarName == "UNIVERSAL_JDBC_DRIVER_PATH":
		AdminConfig.modify(varSubst, [['value', '${WAS_INSTALL_ROOT}/universalDriver/lib']])
	if getVarName == "DB2_JCC_DRIVER_NATIVEPATH":
		AdminConfig.modify(varSubst, [['value', '']])

print 'Starting Creating Mail Providers'
AdminConfig.save()