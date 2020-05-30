
+rem or more contributor license agreements. Licensed under the Elastic License;
+rem you may not use this file except in compliance with the Elastic License.
+
+setlocal enabledelayedexpansion
+setlocal enableextensions
+
+set ES_MAIN_CLASS=org.elasticsearch.xpack.security.authc.saml.SamlMetadataCommand
+set ES_ADDITIONAL_SOURCES=x-pack-env;x-pack-security-env
+call "%~dp0elasticsearch-cli.bat" ^
+  %%* ^
+  || goto exit
+
+endlocal
+endlocal
+:exit
+exit /b %ERRORLEVEL%
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-service-mgr.exe b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-service-mgr.exe
new file mode 100644
index 0000000000000000000000000000000000000000..e5d4b55d91628e9ade6d2612513378f43c9682d6
GIT binary patch
literal 118184
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