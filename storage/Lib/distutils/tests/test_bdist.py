_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-node
new file mode 100644
index 0000000000000000000000000000000000000000..29949486b5526d7812bb09c8286432abd216540f
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-node
@@ -0,0 +1,5 @@
+#!/bin/bash
+
+ES_MAIN_CLASS=org.elasticsearch.cluster.coordination.NodeToolCli \
+  "`dirname "$0"`"/elasticsearch-cli \
+  "$@"
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-node.bat b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-node.bat
new file mode 100644
index 0000000000000000000000000000000000000000..b152331d5ef89c2d04fa78d50643b784b5b034a0
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-node.bat
@@ -0,0 +1,14 @@
+@echo off
+
+setlocal enabledelayedexpansion
+setlocal enableextensions
+
+set ES_MAIN_CLASS=org.elasticsearch.cluster.coordination.NodeToolCli
+call "%~dp0elasticsearch-cli.bat" ^
+  %%* ^
+  || goto exit
+
+endlocal
+endlocal
+:exit
+exit /b %ERRORLEVEL%
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-plugin b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-plugin
new file mode 100644
index 0000000000000000000000000000000000000000..1c11cfb35f235b18c33e116bd92e81735c75f440
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-plugin
@@ -0,0 +1,6 @@
+#!/bin/bash
+
+ES_MAIN_CLASS=org.elasticsearch.plugins.PluginCli \
+  ES_ADDITIONAL_CLASSPAT