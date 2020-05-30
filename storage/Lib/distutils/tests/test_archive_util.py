arch-7.7.0/bin/elasticsearch-cli.bat b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-cli.bat
new file mode 100644
index 0000000000000000000000000000000000000000..866e8efc6689bd544c9afa3710aee2d01bb24e56
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-cli.bat
@@ -0,0 +1,29 @@
+call "%~dp0elasticsearch-env.bat" || exit /b 1
+
+if defined ES_ADDITIONAL_SOURCES (
+  for %%a in ("%ES_ADDITIONAL_SOURCES:;=","%") do (
+    call "%~dp0%%a"
+  )
+)
+
+if defined ES_ADDITIONAL_CLASSPATH_DIRECTORIES (
+  for %%a in ("%ES_ADDITIONAL_CLASSPATH_DIRECTORIES:;=","%") do (
+    set ES_CLASSPATH=!ES_CLASSPATH!;!ES_HOME!/%%a/*
+  )
+)
+
+rem use a small heap size for the CLI tools, and thus the serial collector to
+rem avoid stealing many CPU cycles; a user can override by setting ES_JAVA_OPTS
+set ES_JAVA_OPTS=-Xms4m -Xmx64m -XX:+UseSerialGC %ES_JAVA_OPTS%
+
+%JAVA% ^
+  %ES_JAVA_OPTS% ^
+  -Des.path.home="%ES_HOME%" ^
+  -Des.path.conf="%ES_PATH_CONF%" ^
+  -Des.distribution.flavor="%ES_DISTRIBUTION_FLAVOR%" ^
+  -Des.distribution.type="%ES_DISTRIBUTION_TYPE%" ^
+  -cp "%ES_CLASSPATH%" ^
+  "%ES_MAIN_CLASS%" ^
+  %*
+
+exit /b %ERRORLEVEL%
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-croneval b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-croneval
new file mode 100644
index 0000000000000000000000000000000000000000..1c55587f5562c54ee2ba4df4d6d5bbdd1485cd21
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-croneval
@@ -0,0 +1,10 @@
+#!/bin/bash
+
+# Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
+# or more contributor license agreements. Licensed under the Elastic License;
+# you may not use this file except in compliance with the Elastic License.
+
+ES_MAIN_CLASS=org.elasticsearch.xpack.watcher.trigger.schedule.tool.CronEvalTool \
+  ES_ADDITIONAL_SOURCES="x-pack-env;x-pack-watcher-env" \
+  "`dirname "$0"`"/elasticsearch-cli \
+  "$@"
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-croneval.bat b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-croneval.bat
new file mode 100644
index 0000000000000000000000000000000000000000..571c19056bb96d9994373c0fe5b511a14f79faa4
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-croneval.bat
@@ -0,0 +1,19 @@
+@echo off
+
+rem Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
+rem or more contributor license agreements. Licensed under the Elastic License;
+rem you may not use this file except in compliance with the Elastic License.
+
+setlocal enabledelayedexpansion
+setlocal enableextensions
+
+set ES_MAIN_CLASS=org.elasticsearch.xpack.watcher.trigger.schedule.tool.CronEvalTool
+set ES_ADDITIONAL_SOURCES=x-pack-env;x-pack-watcher-env
+call "%~dp0elasticsearch-cli.bat" ^
+  %%* ^
+  || goto exit
+
+endlocal
+endlocal
+:exit
+exit /b %ERRORLEVEL%
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-env b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-env
new file mode 100644
index 0000000000000000000000000000000000000000..ddd57fcbd9030787be2d99e3df6df78851f21686
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-env
@@ -0,0 +1,142 @@
+#!/bin/bash
+
+set -e -o pipefail
+
+CDPATH=""
+
+SCRIPT="$0"
+
+# SCRIPT might be an arbitrarily deep series of symbolic links; loop until we
+# have the concrete path
+while [ -h "$SCRIPT" ] ; do
+  ls=`ls -ld "$SCRIPT"`
+  # Drop everything prior to ->
+  link=`expr "$ls" : '.*-> \(.*\)$'`
+  if expr "$link" : '/.*' > /dev/null; then
+    SCRIPT="$link"
+  else
+    SCRIPT=`dirname "$SCRIPT"`/"$link"
+  fi
+done
+
+# determine Elasticsearch home; to do this, we strip from the path until we find
+# bin, and then strip bin (there is an assumption here that there is no nested
+# directory under bin also named bin)
+ES_HOME=`dirname "$SCRIPT"`
+
+# now make ES_HOME absolute
+ES_HOME=`cd "$ES_HOME"; pwd`
+
+while [ "`basename "$ES_HOME"`" != "bin" ]; do
+  ES_HOME=`dirname "$ES_HOME"`
+done
+ES_HOME=`dirname "$ES_HOME"`
+
+# now set the classpath
+ES_CLASSPATH="$ES_HOME/lib/*"
+
+# now set the path to java
+if [ ! -z "$JAVA_HOME" ]; then
+  JAVA="$JAVA_HOME/bin/java"
+  JAVA_TYPE="JAVA_HOME"
+else
+  if [ "$(uname -s)" = "Darwin" ]; then
+    # macOS has a different structure
+    JAVA="$ES_HOME/jdk.app/Contents/Home/bin/java"
+  else
+    JAVA="$ES_HOME/jdk/bin/java"
+  fi
+  JAVA_TYPE="bundled jdk"
+fi
+
+if [ ! -x "$JAVA" ]; then
+    echo "could not find java in $JAVA_TYPE at $JAVA" >&2
+    exit 1
+  fi
+
+# do not let JAVA_TOOL_OPTIONS slip in (as the JVM does by default)
+if [ ! -z "$JAVA_TOOL_OPTIONS" ]; then
+  echo "warning: ignoring JAVA_TOOL_OPTIONS=$JAVA_TOOL_OPTIONS"
+  unset JAVA_TOOL_OPTIONS
+fi
+
+# JAVA_OPTS is not a built-in JVM mechanism but some people think it is so we
+# warn them that we are not observing the value of $JAVA_OPTS
+if [ ! -z "$JAVA_OPTS" ]; then
+  echo -n "warning: ignoring JAVA_OPTS=$JAVA_OPTS; "
+  echo "pass JVM parameters via ES_JAVA_OPTS"
+fi
+
+if [[ "$("$JAVA" -version 2>/dev/null)" =~ "Unable to map CDS archive" ]]; then
+  XSHARE="-Xshare:off"
+else
+  XSHARE="-Xshare:auto"
+fi
+
+# check the Java version
+"$JAVA" "$XSHARE" -cp "$ES_CLASSPATH" org.elasticsearch.tools.java_version_checker.JavaVersionChecker
+
+export HOSTNAME=$HOSTNAME
+
+if [ -z "$ES_PATH_CONF" ]; then ES_PATH_CONF="$ES_HOME"/config; fi
+
+if [ -z "$ES_PATH_CONF" ]; then
+  echo "ES_PATH_CONF must be set to the configuration path"
+  exit 1
+fi
+
+# now make ES_PATH_CONF absolute
+ES_PATH_CONF=`cd "$ES_PATH_CONF"; pwd`
+
+ES_DISTRIBUTION_FLAVOR=default
+ES_DISTRIBUTION_TYPE=zip
+ES_BUNDLED_JDK=true
+
+if [[ "$ES_DISTRIBUTION_TYPE" == "docker" ]]; then
+  # Allow environment variables to be set by creating a file with the
+  # contents, and setting an environment variable with the suffix _FILE to
+  # point to it. This can be used to provide secrets to a container, without
+  # the values being specified explicitly when running the container.
+  source "$ES_HOME/bin/elasticsearch-env-from-file"
+
+  # Parse Docker env vars to customize Elasticsearch
+  #
+  # e.g. Setting the env var cluster.name=testcluster
+  #
+  # will cause Elasticsearch to be invoked with -Ecluster.name=testcluster
+  #
+  # see https://www.elastic.co/guide/en/elasticsearch/reference/current/settings.html#_setting_default_settings
+
+  declare -a es_arg_array
+
+  while IFS='=' read -r envvar_key envvar_value
+  do
+    # Elasticsearch settings need to have at least two dot separated lowercase
+    # words, e.g. `cluster.name`
+    if [[ "$envvar_key" =~ ^[a-z0-9_]+\.[a-z0-9_]+ ]]; then
+      if [[ ! -z $envvar_value ]]; then
+        es_opt="-E${envvar_key}=${envvar_value}"
+        es_arg_array+=("${es_opt}")
+      fi
+    fi
+  done < <(env)
+
+  # Reset the positional parameters to the es_arg_array values and any existing positional params
+  set -- "$@" "${es_arg_array[@]}"
+
+  # The virtual file /proc/self/cgroup should list the current cgroup
+  # membership. For each hierarchy, you can follow the cgroup path from
+  # this file to the cgroup filesystem (usually /sys/fs/cgroup/) and
+  # introspect the statistics for the cgroup for the given
+  # hierarchy. Alas, Docker breaks this by mounting the container
+  # statistics at the root while leaving the cgroup paths as the actual
+  # paths. Therefore, Elasticsearch provides a mechanism to override
+  # reading the cgroup path from /proc/self/cgroup and instead uses the
+  # cgroup path defined the JVM system property
+  # es.cgroups.hierarchy.override. Therefore, we set this value here so
+  # that cgroup statistics are available for the container this process
+  # will run in.
+  export ES_JAVA_OPTS="-Des.cgroups.hierarchy.override=/ $ES_JAVA_OPTS"
+fi
+
+cd "$ES_HOME"
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-env-from-file b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-env-from-file
new file mode 100644
index 0000000000000000000000000000000000000000..c34e9cafb9e45c614f0b1fa52c7a8744fc9b7632
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-env-from-file
@@ -0,0 +1,50 @@
+#!/bin/bash
+
+set -e -o pipefail
+
+# Allow environment variables to be set by creating a file with the
+# contents, and setting an environment variable with the suffix _FILE to
+# point to it. This can be used to provide secrets to a container, without
+# the values being specified explicitly when running the container.
+#
+# Note that only supported environment variables are processed, in order
+# to avoid unexpected failures when an environment sets a "*_FILE" variable
+# that doesn't contain a filename.
+#
+# This script is intended to be sourced, not executed, and modifies the
+# environment.
+
+for VAR_NAME_FILE in ELASTIC_PASSWORD_FILE KEYSTORE_PASSWORD_FILE ; do
+  if [[ -n "${!VAR_NAME_FILE}" ]]; then
+    VAR_NAME="${VAR_NAME_FILE%_FILE}"
+
+    if env | grep "^${VAR_NAME}="; then
+      echo "ERROR: Both $VAR_NAME_FILE and $VAR_NAME are set. These are mutually exclusive." >&2
+      exit 1
+    fi
+
+    if [[ ! -e "${!VAR_NAME_FILE}" ]]; then
+      echo "ERROR: File ${!VAR_NAME_FILE} from $VAR_NAME_FILE does not exist" >&2
+      exit 1
+    fi
+
+    FILE_PERMS="$(stat -L -c '%a' ${!VAR_NAME_FILE})"
+
+    if [[ "$FILE_PERMS" != "400" && "$FILE_PERMS" != "600" ]]; then
+        if [[ -h "${!VAR_NAME_FILE}" ]]; then
+            echo "ERROR: File $(readlink "${!VAR_NAME_FILE}") (target of symlink ${!VAR_NAME_FILE} from $VAR_NAME_FILE) must have file permissions 400 or 600, but actually has: $FILE_PERMS" >&2
+        else
+            echo "ERROR: File ${!VAR_NAME_FILE} from $VAR_NAME_FILE must have file permissions 400 or 600, but actually has: $FILE_PERMS" >&2
+        fi
+        exit 1
+    fi
+
+    echo "Setting $VAR_NAME from $VAR_NAME_FILE at ${!VAR_NAME_FILE}" >&2
+    export "$VAR_NAME"="$(cat ${!VAR_NAME_FILE})"
+
+    unset VAR_NAME
+    # Unset the suffixed environment variable
+    unset "$VAR_NAME_FILE"
+  fi
+done
+
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-env.bat b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-env.bat
new file mode 100644
index 0000000000000000000000000000000000000000..73e0681b41394fa9906eca2ac5be7e71a37440cb
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-env.bat
@@ -0,0 +1,68 @@
+set SCRIPT=%0
+
+rem determine Elasticsearch home; to do this, we strip from the path until we
+rem find bin, and then strip bin (there is an assumption here that there is no
+rem nested directory under bin also named bin)
+for %%I in (%SCRIPT%) do set ES_HOME=%%~dpI
+
+:es_home_loop
+for %%I in ("%ES_HOME:~1,-1%") do set DIRNAME=%%~nxI
+if not "%DIRNAME%" == "bin" (
+  for %%I in ("%ES_HOME%..") do set ES_HOME=%%~dpfI
+  goto es_home_loop
+)
+for %%I in ("%ES_HOME%..") do set ES_HOME=%%~dpfI
+
+rem now set the classpath
+set ES_CLASSPATH=!ES_HOME!\lib\*
+
+set HOSTNAME=%COMPUTERNAME%
+
+if not defined ES_PATH_CONF (
+  set ES_PATH_CONF=!ES_HOME!\config
+)
+
+rem now make ES_PATH_CONF absolute
+for %%I in ("%ES_PATH_CONF%..") do set ES_PATH_CONF=%%~dpfI
+
+set ES_DISTRIBUTION_FLAVOR=default
+set ES_DISTRIBUTION_TYPE=zip
+set ES_BUNDLED_JDK=true
+
+cd /d "%ES_HOME%"
+
+rem now set the path to java, pass "nojava" arg to skip setting JAVA_HOME and JAVA
+if "%1" == "nojava" (
+   exit /b
+)
+
+if defined JAVA_HOME (
+  set JAVA="%JAVA_HOME%\bin\java.exe"
+  set JAVA_TYPE=JAVA_HOME
+) else (
+  set JAVA="%ES_HOME%\jdk\bin\java.exe"
+  set JAVA_HOME="%ES_HOME%\jdk"
+  set JAVA_TYPE=bundled jdk
+)
+
+if not exist !JAVA! (
+  echo "could not find java in !JAVA_TYPE! at !JAVA!" >&2
+  exit /b 1
+)
+
+rem do not let JAVA_TOOL_OPTIONS slip in (as the JVM does by default)
+if defined JAVA_TOOL_OPTIONS (
+  echo warning: ignoring JAVA_TOOL_OPTIONS=%JAVA_TOOL_OPTIONS%
+  set JAVA_TOOL_OPTIONS=
+)
+
+rem JAVA_OPTS is not a built-in JVM mechanism but some people think it is so we
+rem warn them that we are not observing the value of %JAVA_OPTS%
+if defined JAVA_OPTS (
+  (echo|set /p=warning: ignoring JAVA_OPTS=%JAVA_OPTS%; )
+  echo pass JVM parameters via ES_JAVA_OPTS
+)
+
+rem check the Java version
+%JAVA% -cp "%ES_CLASSPATH%" "org.elasticsearch.tools.java_version_checker.JavaVersionChecker" || exit /b 1
+
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-keystore b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-keystore
new file mode 100644
index 0000000000000000000000000000000000000000..49e1aa7437a0851f5dc1eb384969cf2dc7d3610e
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-keystore
@@ -0,0 +1,5 @@
+#!/bin/bash
+
+ES_MAIN_CLASS=org.elasticsearch.common.settings.KeyStoreCli \
+  "`dirname "$0"`"/elasticsearch-cli \
+  "$@"
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-keystore.bat b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-keystore.bat
new file mode 100644
index 0000000000000000000000000000000000000000..83372248fb61a18be8eb4d6af6cbde5fd9dfb746
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-keystore.bat
@@ -0,0 +1,14 @@
+@echo off
+
+setlocal enabledelayedexpansion
+setlocal enableextensions
+
+set ES_MAIN_CLASS=org.elasticsearch.common.settings.KeyStoreCli
+call "%~dp0elasticsearch-cli.bat" ^
+  %%* ^
+  || goto exit
+
+endlocal
+endlocal
+:exit
+exit /b %ERRORLEVEL%
diff --git a/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-migrate b/file_drive-master/content/assets/elasticsearch-7.7.0/elasticsearch-7.7.0/bin/elasticsearch-migrate
new file mode 100644
index 0000000000000000000000000000000000000000..183722d9c9364899d39c24f5cefeb8e059e70b60
--- /dev/null
+++ b/file_drive-master/content/assets/elasticsear