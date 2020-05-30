rname "$0"`"/elasticsearch-env
+
+CHECK_KEYSTORE=true
+DAEMONIZE=false
+for option in "$@"; do
+  case "$option" in
+    -h|--help|-V|--version)
+      CHECK_KEYSTORE=false
+      ;;
+    -d|--daemonize)
+      DAEMONIZE=true
+      ;;
+  esac
+done
+
+if [ -z "$ES_TMPDIR" ]; then
+  ES_TMPDIR=`"$JAVA" "$XSHARE" -cp "$ES_CLASSPATH" org.elasticsearch.tools.launchers.TempDirectory`
+fi
+
+# get keystore password before setting java options to avoid
+# conflicting GC configurations for the keystore tools
+unset KEYSTORE_PASSWORD
+KEYSTORE_PASSWORD=
+if [[ $CHECK_KEYSTORE = true ]] \
+    && bin/elasticsearch-keystore has-passwd --silent
+then
+  if ! read -s -r -p "Elasticsearch keystore password: " KEYSTORE_PASSWORD ; then
+    echo "Failed to read keystore password on console" 1>&2
+    exit 1
+  fi
+fi
+
+# The JVM options parser produces the final JVM options to start Elasticsearch.
+# It does this by incorporating JVM options in the following way:
+#   - first, system JVM options are applied (these are hardcoded options in the
+#     parser)
+#   - second, JVM options are read from jvm.options and jvm.options.d/*.options
+#   - third, JVM options from ES_JAVA_OPTS are applied
+#   - fourth, ergonomic JVM options are applied
+ES_JAVA_OPTS=`export ES_TMPDIR; "$JAVA" "$XSHARE" -cp "$ES_CLASSPATH" org.elasticsearch.tools.launchers.JvmOptionsParser "$ES_PATH_CONF"`
+
+# manual parsing to find out, if process should be detached
+if [[ $DAEMONIZE = false ]]; then
+  exec \
+    "$JAVA" \
+    "$XSHARE" \
+    $ES_JAVA_OPTS \
+    -Des.path.home="$ES_HOME" \
+    -Des.path.conf="$ES_PATH_CONF" \
+    -Des.distribution.flavor="$ES_DISTRIBUTION_FLAVOR" \
+    -Des.distribution.type="$ES_DISTRIBUTION_TYPE" \
+    -Des.bundled_jdk="$ES_BUNDLED_JDK" \
+    -cp "$ES_CLASSPATH" \
+    org.elasticsearch.bootstrap.Elasticsearch \
+    "$@" <<<"$KEYSTORE_PASSWORD"
+else
+  exec \
+    "$JAVA" \
+    "$XSHARE" \
+    $ES_JAVA_OPTS \
+    -Des.path.home="$ES_HOME" \
+    -Des.path.conf="$ES_PATH_CONF" \
+    -Des.distribution.flavor="$ES_DISTRIBUTION_FLAVOR" \
+    -Des.distribution.type="$ES_DISTRIBUTION_TYPE" \
+    -Des.bundled_jdk="$ES_BUNDLED_JDK" \
+    -cp "$ES_CLASSPATH" \
+    org.elasticsearch.bootstrap.Elasticsearch \
+    "$@" \
+    <<<"$KEYSTORE_PASSWORD" &
+  retval=$?
+  pid=$!
+  [ $retval -eq 0 ] || exit $retval
+  if [ ! -z "$ES_STARTUP_SLEEP_TIME" ]; then
+    sleep $ES_STARTUP_SLEEP_TIME
+  fi
+  if ! ps -p $pid > /dev/null ; then
+    exit 1
+  fi
+  exit 0
+fi
+
+exit $?
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certgen b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certgen
new file mode 100644
index 0000000000000000000000000000000000000000..8e88e845e024283577376ec33a34b26b55b4a9a1
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certgen
@@ -0,0 +1,11 @@
+#!/bin/bash
+
+# Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
+# or more contributor license agreements. Licensed under the Elastic License;
+# you may not use this file except in compliance with the Elastic License.
+
+ES_MAIN_CLASS=org.elasticsearch.xpack.security.cli.CertificateGenerateTool \
+  ES_ADDITIONAL_SOURCES="x-pack-env;x-pack-security-env" \
+  ES_ADDITIONAL_CLASSPATH_DIRECTORIES=lib/tools/security-cli \
+  "`dirname "$0"`"/elasticsearch-cli \
+  "$@"
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certgen.bat b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certgen.bat
new file mode 100644
index 0000000000000000000000000000000000000000..d268ea04290dd0d279a09839bec151a83bef42c3
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certgen.bat
@@ -0,0 +1,20 @@
+@echo off
+
+rem Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
+rem or more contributor license agreements. Licensed under the Elastic License;
+rem you may not use this file except in compliance with the Elastic License.
+
+setlocal enabledelayedexpansion
+setlocal enableextensions
+
+set ES_MAIN_CLASS=org.elasticsearch.xpack.security.cli.CertificateGenerateTool
+set ES_ADDITIONAL_SOURCES=x-pack-env;x-pack-security-env
+set ES_ADDITIONAL_CLASSPATH_DIRECTORIES=lib/tools/security-cli
+call "%~dp0elasticsearch-cli.bat" ^
+  %%* ^
+  || goto exit
+
+endlocal
+endlocal
+:exit
+exit /b %ERRORLEVEL%
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certutil b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certutil
new file mode 100644
index 0000000000000000000000000000000000000000..6d94344949b9bc66a02cc66e8100e68987c1c268
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certutil
@@ -0,0 +1,11 @@
+#!/bin/bash
+
+# Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
+# or more contributor license agreements. Licensed under the Elastic License;
+# you may not use this file except in compliance with the Elastic License.
+
+ES_MAIN_CLASS=org.elasticsearch.xpack.security.cli.CertificateTool \
+  ES_ADDITIONAL_SOURCES="x-pack-env;x-pack-security-env" \
+  ES_ADDITIONAL_CLASSPATH_DIRECTORIES=lib/tools/security-cli \
+  "`dirname "$0"`"/elasticsearch-cli \
+  "$@"
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certutil.bat b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certutil.bat
new file mode 100644
index 0000000000000000000000000000000000000000..40dc4f5c29b4f6bb89fd9fc19c3fd118e856d070
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-certutil.bat
@@ -0,0 +1,20 @@
+@echo off
+
+rem Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
+rem or more contributor license agreements. Licensed under the Elastic License;
+rem you may not use this file except in compliance with the Elastic License.
+
+setlocal enabledelayedexpansion
+setlocal enableextensions
+
+set ES_MAIN_CLASS=org.elasticsearch.xpack.security.cli.CertificateTool
+set ES_ADDITIONAL_SOURCES=x-pack-env;x-pack-security-env
+set ES_ADDITIONAL_CLASSPATH_DIRECTORIES=lib/tools/security-cli
+call "%~dp0elasticsearch-cli.bat" ^
+  %%* ^
+  || goto exit
+
+endlocal
+endlocal
+:exit
+exit /b %ERRORLEVEL%
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearc