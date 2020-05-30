
 .../demos/customPosition.html                 |    78 +
 .../basicContext-master/demos/default.html    |    79 +
 .../basicContext-master/demos/jQuery.html     |    80 +
 .../basicContext-master/demos/position.html   |   113 +
 .../basicContext-master/demos/scroll.html     |   143 +
 .../demos/themes/bright.html                  |   143 +
 .../demos/themes/dark.html                    |   143 +
 .../demos/themes/default.html                 |   143 +
 .../dist/addons/fadein.min.css                |     1 +
 .../dist/addons/popin.min.css                 |     1 +
 .../dist/basicContext.min.css                 |     1 +
 .../dist/basicContext.min.js                  |     1 +
 .../dist/themes/bright.min.css                |     1 +
 .../dist/themes/dark.min.css                  |     1 +
 .../dist/themes/default.min.css               |     1 +
 .../dist/themes/light.min.css                 |     1 +
 .../assets/basicContext-master/gulpfile.js    |    65 +
 .../assets/basicContext-master/js_test.html   |    77 +
 .../assets/basicContext-master/package.json   |    37 +
 .../assets/basicContext-master/readme.md      |   137 +
 .../src/scripts/basicContext.js               |   264 +
 .../src/styles/_container.scss                |    11 +
 .../src/styles/_context.scss                  |    50 +
 .../basicContext-master/src/styles/_vars.scss |     2 +
 .../src/styles/addons/fadein.scss             |    12 +
 .../src/styles/addons/popin.scss              |    12 +
 .../basicContext-master/src/styles/main.scss  |     6 +
 .../src/styles/themes/bright.scss             |    50 +
 .../src/styles/themes/dark.scss               |    48 +
 .../src/styles/themes/default.scss            |    50 +
 .../content/assets/css/dialog.css             |   130 +
 .../content/assets/css/styles.css             |   434 +
 .../elasticsearch-7.7.0/LICENSE.txt           |   223 +
 .../elasticsearch-7.7.0/NOTICE.txt            |  9863 ++
 .../elasticsearch-7.7.0/README.asciidoc       |   209 +
 .../elasticsearch-7.7.0/bin/elasticsearch     |    97 +
 .../bin/elasticsearch-certgen                 |    11 +
 .../bin/elasticsearch-certgen.bat             |    20 +
 .../bin/elasticsearch-certutil                |    11 +
 .../bin/elasticsearch-certutil.bat            |    20 +
 .../elasticsearch-7.7.0/bin/elasticsearch-cli |    33 +
 .../bin/elasticsearch-cli.bat                 |    29 +
 .../bin/elasticsearch-croneval                |    10 +
 .../bin/elasticsearch-croneval.bat            |    19 +
 .../elasticsearch-7.7.0/bin/elasticsearch-env |   142 +
 .../bin/elasticsearch-env-from-file           |    50 +
 .../bin/elasticsearch-env.bat                 |    68 +
 .../bin/elasticsearch-keystore                |     5 +
 .../bin/elasticsearch-keystore.bat            |    14 +
 .../bin/elasticsearch-migrate                 |    10 +
 .../bin/elasticsearch-migrate.bat             |    19 +
 .../bin/elasticsearch-node                    |     5 +
 .../bin/elasticsearch-node.bat                |    14 +
 .../bin/elasticsearch-plugin                  |     6 +
 .../bin/elasticsearch-plugin.bat              |    16 +
 .../bin/elasticsearch-saml-metadata           |    10 +
 .../bin/elasticsearch-saml-metadata.bat       |    19 +
 .../bin/elasticsearch-service-mgr.exe         |   Bin 0 -> 118184 bytes
 .../bin/elasticsearch-service-x64.exe         |   Bin 0 -> 114600 bytes
 .../bin/elasticsearch-service.bat             |   286 +
 .../bin/elasticsearch-setup-passwords         |    10 +
 .../bin/elasticsearch-setup-passwords.bat     |    19 +
 .../bin/elasticsearch-shard                   |     5 +
 .../bin/elasticsearch-shard.bat               |    14 +
 .../bin/elasticsearch-sql-cli                 |    17 +
 .../bin/elasticsearch-sql-cli-7.7.0.jar       |   Bin 0 -> 20565600 bytes
 .../bin/elasticsearch-sql-cli.bat             |    25 +
 .../bin/elasticsearch-syskeygen               |    10 +
 .../bin/elasticsearch-syskeygen.bat           |    19 +
 .../bin/elasticsearch-users                   |    10 +
 .../bin/elasticsearch-users.bat               |    19 +
 .../elasticsearch-7.7.0/bin/elasticsearch.bat |   109 +
 .../elasticsearch-7.7.0/bin/x-pack-env        |     8 +
 .../elasticsearch-7.7.0/bin/x-pack-env.bat    |     5 +
 .../bin/x-pack-security-env                   |     8 +
 .../bin/x-pack-security-env.bat               |     5 +
 .../bin/x-pack-watcher-env                    |     8 +
 .../bin/x-pack-watcher-env.bat                |     5 +
 .../config/elasticsearch.keystore             |   Bin 0 -> 199 bytes
 .../config/elasticsearch.yml                  |    88 +
 .../elasticsearch-7.7.0/config/jvm.options    |    77 +
 .../config/log4j2.properties                  |   259 +
 .../config/role_mapping.yml                   |    14 +
 .../elasticsearch-7.7.0/config/roles.yml      |     3 +
 .../elasticsearch-7.7.0/config/users          |     0
 .../elasticsearch-7.7.0/config/users_roles    |     0
 .../data/nodes/0/_state/_r.cfe                |   Bin 0 -> 246 bytes
 .../data/nodes/0/_state/_r.cfs                |   Bin 0 -> 13892 bytes
 .../data/nodes/0/_state/_r.si                 |   Bin 0 -> 350 bytes
 .../data/nodes/0/_state/manifest-0.st         |   Bin 0 -> 109 bytes
 .../data/nodes/0/_state/node-0.st             |   Bin 0 -> 89 bytes
 .../data/nodes/0/_state/segments_v            |   Bin 0 -> 229 bytes
 .../data/nodes/0/_state/write.lock            |     0
 .../data/nodes/0/node.lock                    |     0
 .../bin/api-ms-win-core-console-l1-1-0.dll    |   Bin 0 -> 9688 bytes
 .../bin/api-ms-win-core-datetime-l1-1-0.dll   |   Bin 0 -> 9176 bytes
 .../jdk/bin/api-ms-win-core-debug-l1-1-0.dll  |   Bin 0 -> 9176 bytes
 .../api-ms-win-core-errorhandling-l1-1-0.dll  |   Bin 0 -> 9176 bytes
 .../jdk/bin/api-ms-win-core-file-l1-1-0.dll   |   Bin 0 -> 12760 bytes
 .../jdk/bin/api-ms-win-core-file-l1-2-0.dll   |   Bin 0 -> 9176 bytes
 .../jdk/bin/api-ms-win-core-file-l2-1-0.dll   |   Bin 0 -> 9176 bytes
 .../jdk/bin/api-ms-win-core-handle-l1-1-0.dll |   Bin 0 -> 9176 bytes
 .../jdk/bin/api-ms-win-core-heap-l1-1-0.dll   |   Bin 0 -> 9688 bytes
 .../api-ms-win-core-interlocked-l1-1-0.dll    |   Bin 0 -> 9176 bytes
 .../api-ms-win-core-libraryloader-l1-1-0.dll  |   Bin 0 -> 10200 bytes
 .../api-ms-win-core-localization-l1-2-0.dll   |   Bin 0 -> 11736 bytes
 .../jdk/bin/api-ms-win-core-memory-l1-1-0.dll |   Bin 0 -> 9688 bytes
 .../bin/api-ms-win-core-namedpipe-l1-1-0.dll  |   Bin 0 -> 9176 bytes
 ...-ms-win-core-processenvironment-l1-1-0.dll |   Bin 0 -> 10200 bytes
 .../api-ms-win-core-processthreads-l1-1-0.dll |   Bin 0 -> 11224 bytes
 .../api-ms-win-core-processthreads-l1-1-1.dll |   Bin 0 -> 9688 bytes
 .../bin/api-ms-win-core-profile-l1-1-0.dll    |   Bin 0 -> 8664 bytes
 .../bin/api-ms-win-core-rtlsupport-l1-1-0.dll |   Bin 0 -> 9688 bytes
 .../jdk/bin/api-ms-win-core-string-l1-1-0.dll |   Bin 0 -> 9176 bytes
 .../jdk/bin/api-ms-win-core-synch-l1-1-0.dll  |   Bin 0 -> 11224 bytes
 .../jdk/bin/api-ms-win-core-synch-l1-2-0.dll  |   Bin 0 -> 9688 bytes
 .../bin/api-ms-win-core-sysinfo-l1-1-0.dll    |   Bin 0 -> 10200 bytes
 .../bin/api-ms-win-core-timezone-l1-1-0.dll   |   Bin 0 -> 9688 bytes
 .../jdk/bin/api-ms-win-core-util-l1-1-0.dll   |   Bin 0 -> 9176 bytes
 .../jdk/bin/api-ms-win-crt-conio-l1-1-0.dll   |   Bin 0 -> 10200 bytes
 .../jdk/bin/api-ms-win-crt-convert-l1-1-0.dll |   Bin 0 -> 13272 bytes
 .../bin/api-ms-win-crt-environment-l1-1-0.dll |   Bin 0 -> 9688 bytes
 .../bin/api-ms-win-crt-filesystem-l1-1-0.dll  |   Bin 0 -> 11224 bytes
 .../jdk/bin/api-ms-win-crt-heap-l1-1-0.dll    |   Bin 0 -> 10200 bytes
 .../jdk/bin/api-ms-win-crt-locale-l1-1-0.dll  |   Bin 0 -> 9688 bytes
 .../jdk/bin/api-ms-win-crt-math-l1-1-0.dll    |   Bin 0 -> 18392 bytes
 .../bin/api-ms-win-crt-multibyte-l1-1-0.dll   |   Bin 0 -> 17368 bytes
 .../jdk/bin/api-ms-win-crt-private-l1-1-0.dll |   Bin 0 -> 61912 bytes
 .../jdk/bin/api-ms-win-crt-process-l1-1-0.dll |   Bin 0 -> 10200 bytes
 .../jdk/bin/api-ms-win-crt-runtime-l1-1-0.dll |   Bin 0 -> 13784 bytes
 .../jdk/bin/api-ms-win-crt-stdio-l1-1-0.dll   |   Bin 0 -> 15320 bytes
 .../jdk/bin/api-ms-win-crt-string-l1-1-0.dll  |   Bin 0 -> 15320 bytes
 .../jdk/bin/api-ms-win-crt-time-l1-1-0.dll    |   Bin 0 -> 11736 bytes
 .../jdk/bin/api-ms-win-crt-utility-l1-1-0.dll |   Bin 0 -> 9688 bytes
 .../elasticsearch-7.7.0/jdk/bin/attach.dll    |   Bin 0 -> 24536 bytes
 .../elasticsearch-7.7.0/jdk/bin/awt.dll       |   Bin 0 -> 1512408 bytes
 .../jdk/bin/client/jvm.dll                    |   Bin 0 -> 7120856 bytes
 .../elasticsearch-7.7.0/jdk/bin/dt_shmem.dll  |   Bin 0 -> 32728 bytes
 .../elasticsearch-7.7.0/jdk/bin/dt_socket.dll |   Bin 0 -> 31192 bytes
