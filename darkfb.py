<!doctype html><html class="no-js" dir="ltr" loc="en" manifest=""><head><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><title>WhatsApp Web</title><meta name="viewport" content="width=device-width"><meta name="google" content="notranslate"><meta name="format-detection" content="telephone=no"><meta name="description" content="Quickly send and receive WhatsApp messages right from your computer."><meta name="og:description" content="Quickly send and receive WhatsApp messages right from your computer."><meta name="og:url" content="https://web.whatsapp.com/"><meta name="og:title" content="WhatsApp Web"><meta name="og:image" content="https://static.facebook.com/images/whatsapp/www/whatsapp-promo.png"><link id="favicon" rel="shortcut icon" href="/img/favicon/1x/favicon.png" type="image/png"><link rel="apple-touch-icon" sizes="194x194" href="/apple-touch-icon.png" type="image/png"><link rel="stylesheet" href="/cssm_qr.d4d58b58ca1d17502d79b048006a9f17.css"><style>html, body, #app {
              height: 100%;
              width: 100%;
              overflow: hidden;
              padding: 0;
              margin: 0;
          }

          #app {
              position: absolute;
              top: 0;
              left: 0;
          }

          #startup, #initial_startup {
              width: 100%;
              height: 100%;
              position: fixed;
              background-color: #f2f2f2;

              -moz-user-select: none;
              -webkit-user-select: none;

              display: flex;
              align-items: center;
              justify-content: center;
              display: -webkit-box;
              display: -webkit-flex;
              -webkit-align-items: center;
              -webkit-justify-content: center;
              flex-direction: column;
              -webkit-flex-direction: column;
          }

          .spinner-container {
              -webkit-animation: rotate 2s linear infinite;
                      animation: rotate 2s linear infinite;
              z-index: 2;
          }

          .spinner-path {
              stroke-dasharray: 1,150; /* 1%, 101% circumference */
              stroke-dashoffset: 0;
              stroke: #acb9bf;
              stroke-linecap: round;
              -webkit-animation: dash 1.5s ease-in-out infinite;
                      animation: dash 1.5s ease-in-out infinite;
          }

          @keyframes rotate {
              100% { transform: rotate(360deg); }
          }
          @-webkit-keyframes rotate{
              100% { -webkit-transform: rotate(360deg); }
          }

          @keyframes dash {
              0% {
                  stroke-dasharray: 1,150;  /* 1%, 101% circumference */
                  stroke-dashoffset: 0;
              }
              50% {
                  stroke-dasharray: 90,150; /* 70%, 101% circumference */
                  stroke-dashoffset: -35;   /* 25% circumference */
              }
              100% {
                  stroke-dasharray: 90,150; /* 70%, 101% circumference */
                  stroke-dashoffset: -124;  /* -99% circumference */
              }
          }
          @-webkit-keyframes dash {
              0% {
                  stroke-dasharray: 1,150;  /* 1%, 101% circumference */
                  stroke-dashoffset: 0;
              }
              50% {
                  stroke-dasharray: 90,150; /* 70%, 101% circumference */
                  stroke-dashoffset: -35;   /* 25% circumference */
              }
              100% {
                  stroke-dasharray: 90,150; /* 70%, 101% circumference */
                  stroke-dashoffset: -124;  /* -99% circumference */
              }
          }

          .progress-container {
            width: 360px;
            position: fixed;
            padding-top: 120px;
            top: 50%;
            left: 50%;
            margin-left: -180px;
          }

          progress {
            -webkit-appearance: none;
            appearance: none;
            width: 100%;
            height: 3px;
            border: none;
            margin: 0;
            color: #02d1a4;
            background-color: #e0e4e5;
          }

          progress[value]::-webkit-progress-bar {
            background-color: #e0e4e5;
          }

          progress[value]::-webkit-progress-value {
              background-color: #02d1a4;
              transition: width 0.3s ease;
          }

          progress[value]::-moz-progress-bar {
              background-color: #02d1a4;
          }</style></head><body class="web"><div id="app" data-app2="/app2.b3a28c95c7e0ca958d18.js" data-app="/app.82261d6b50386f92438b.js" data-vendor1="/vendor1~app.4c3f74a79f6d2099e0d3.js" data-vendor2="/vendors~app2.d7978e31f297370d72f4.js" data-app-size="2271404" data-vendor1-size="1251131" data-vendor2-size="90274" data-cssm-app="/cssm_app.f70b7a02252ed651fedb75a76440a88e.css"></div><div id="hard_expire_time" data-time="1603310013.209"></div><div id="initial_startup"><svg class="spinner-container" width="50" height="50" viewBox="0 0 44 44"><circle class="spinner-path" cx="22" cy="22" r="20" fill="none" stroke-width="4"></circle></svg><div class="progress-container"><progress dir="ltr" id="progressbar" value="0" max="4516011.25"></progress></div></div><script>/*! Copyright (c) 2020 WhatsApp Inc. All Rights Reserved. */!function(e){var r={};function t(n){if(r[n])return r[n].exports;var o=r[n]={i:n,l:!1,exports:{}};return e[n].call(o.exports,o,o.exports,t),o.l=!0,o.exports}t.m=e,t.c=r,t.d=function(e,r,n){t.o(e,r)||Object.defineProperty(e,r,{enumerable:!0,get:n})},t.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},t.t=function(e,r){if(1&r&&(e=t(e)),8&r)return e;if(4&r&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(t.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&r&&"string"!=typeof e)for(var o in e)t.d(n,o,function(r){return e[r]}.bind(null,o));return n},t.n=function(e){var r=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(r,"a",r),r},t.o=function(e,r){return Object.prototype.hasOwnProperty.call(e,r)},t.p="/",t(t.s="dgeiejggee")}({bcceefiggd:function(e,r,t){"use strict";var n=t("cfjecfhbfg");Object.defineProperty(r,"__esModule",{value:!0}),r.default=r.ScriptLoaderClass=void 0;var o=n(t("eaidjcib")),a=n(t("dgcdacjddi")),i=t("dfjdhbagei"),c=n(t("bjiddchbgc")),s=n(t("jegfdjaci")),u=function(){function e(){(0,o.default)(this,e)}return(0,a.default)(e,[{key:"_loadScript",value:function(e){var r=e.src,t=e.size;return new Promise((function(e,n){var o="progress_script_"+r,a=document.getElementById(o);a&&document.head&&document.head.removeChild(a);var i=function(e){return/\.js$/.test(e)}(r)?function(e,r){var t=document.createElement("script");return t.id=r,t.type="text/javascript",t.charset="utf-8",t.src=e,t}(r,o):function(e,r){var t=document.createElement("link");return t.id=r,t.rel="stylesheet",t.href=e,t}(r,o);i.onload=function(){i.onload=i.onerror=void 0,e({progress:t,size:t,src:r})},i.onerror=function(e){i.onload=i.onerror=void 0,n(e)},document.head&&document.head.appendChild(i)}))}},{key:"loadScriptsInParallel",value:function(e,r){var t=this,n=null==r?void 0:r.onProgress,o=[],a=[],i=[],s=e.reduce((function(e,r){return e+r.size}),0),u=new c.default,d=e.map((function(e){return t._loadScript(e).then((function(r){o.push(e),u.updateProgress(r.src,r.progress),n&&n({totalSize:s,progress:u.getProgress()})})).catch((function(r){i.push(r),a.push(e)}))}));return Promise.all(d).then((function(){return{succeededScripts:o,failedScripts:a,errors:i}}))}},{key:"loadInSeriesWithRetry",value:function(e,r){var t=this,n=r.onProgress,o=e.reduce((function(e,r){return e+r.size}),0),a=new c.default;return(0,s.default)(e,(function(e){return t.loadWithRetry(e).then((function(r){return a.updateProgress(e.src,e.size),n&&n({totalSize:o,progress:a.getProgress()}),r}))})).then((function(r){return e.forEach((function(e,t){var n=e.src,o=r[t].errors;o.length&&(0,i.logScriptEventualSuccess)(n,o.length+1)})),{strategy:"series"}}))}},{key:"_series",value:function(e,r){var t=[];return e.reduce((function(e,n,o,a){return e.then((function(){return r(n).then((function(e){return t.push(e),t}))}))}),Promise.resolve())}},{key:"loadWithRetry",value:function(e){var r=this,t=[];return new Promise((function(n){!function o(){return r._loadScript(e).then((function(){return n({errors:t})})).catch((function(r){window.setTimeout(o,Math.min(1e4,1e3*Math.pow(2,t.length))),t.push(r),(0,i.logScriptLoadError)(e.src,t.length)}))}()}))}},{key:"loadScriptsWithFallbackToSeries",value:function(e,r){var t=this,n=null==r?void 0:r.onProgress,o=e.reduce((function(e,r){return e+r.size}),0),a=new c.default;return this.loadScriptsInParallel(e,{onProgress:function(e){a.updateProgress("parallel",e.progress),i()}}).then((function(e){var r=e.failedScripts;return r.length?t.loadInSeriesWithRetry(r,{onProgress:s}).then((function(){return{strategy:"series"}})):{strategy:"parallel"}}));function i(){n&&n({totalSize:o,progress:a.getProgress()})}function s(e){a.updateProgress("series",e.progress),i()}}}]),e}();var d=u;r.ScriptLoaderClass=d;var f=new u;r.default=f},bgbihbeeif:function(e,r,t){"use strict";Object.defineProperty(r,"__esModule",{value:!0}),r.default=function(){var e=document.getElementById("app");if(!e)throw"root element app not found";if(!e.dataset)throw"missing dataset annotations on app for bundles";a([{src:e.dataset.vendor1,size:+e.dataset.vendor1Size},{src:e.dataset.vendor2,size:+e.dataset.vendor2Size},{src:e.dataset.app,size:+e.dataset.appSize}]).then((function(r){var t=[{src:e.dataset.cssmApp,size:0},{src:e.dataset.app2,size:0}],n=r?a(t):i(t);return window.Exe(n.then((function(){}))),n})).catch((function(e){throw(0,n.logProgressError)(e),e}))};var n=t("dfjdhbagei");if(window.onerror=function(e,r,t,o,a){return(0,n.logProgressError)(a),!0},window.navigator.serviceWorker&&!window.navigator.serviceWorker.controller)try{window.navigator.serviceWorker.register("/serviceworker.js",{scope:"/"})}catch(e){}var o=/\.js$/;function a(e){return new Promise((function(r,t){var n=e.length,o=[];e.forEach((function(e){s(e).then((function(t){t||o.push(e),--n>0||(o.length>0&&r(i(o,1)),r(!0))})).catch(t)}))}))}function i(e){var r=arguments.length>1&&void 0!==arguments[1]?arguments[1]:0;return 0===e.length?Promise.resolve(!1):c(e.shift(),r).then((function(){return i(e,r)}))}function c(e,r){return(0,n.logScriptLoadError)(e.src,r),new Promise((function(t){window.setTimeout((function(){t(s(e).then((function(t){if(!t)return c(e,r+1)})))}),1e3*Math.min(r,10))}))}function s(e){var r=e.src,t=e.size;return new Promise((function(e){var n="progress_script_"+r,a=document.getElementById(n);a&&document.head&&document.head.removeChild(a);var i=o.test(r)?function(e,r){var t=document.createElement("script");return t.id=r,t.type="text/javascript",t.charset="utf-8",t.src=e,t}(r,n):function(e,r){var t=document.createElement("link");return t.id=r,t.rel="stylesheet",t.href=e,t}(r,n);i.onload=function(){var r=document.getElementById("progressbar");r&&r.setAttribute("value",String(+r.getAttribute("value")+t)),i.onload=i.onerror=void 0,e(!0)},i.onerror=function(){i.onload=i.onerror=void 0,e(!1)},document.head&&document.head.appendChild(i)}))}},bjiddchbgc:function(e,r,t){"use strict";var n=t("cfjecfhbfg");Object.defineProperty(r,"__esModule",{value:!0}),r.default=void 0;var o=n(t("eaidjcib")),a=n(t("dgcdacjddi")),i=function(){function e(){(0,o.default)(this,e),this._progressMap={}}return(0,a.default)(e,[{key:"updateProgress",value:function(e,r){if(!(r<0)){var t=this._progressMap[e]||0;this._progressMap[e]=Math.max(t,r)}}},{key:"getProgress",value:function(){var e=this;return Object.keys(this._progressMap).reduce((function(r,t){return r+e._progressMap[t]}),0)}}]),e}();r.default=i},cfjecfhbfg:function(e,r){e.exports=function(e){return e&&e.__esModule?e:{default:e}}},cjighbeabh:function(e,r,t){"use strict";function n(e){return e.includes("windows")?"Windows":e.includes("mac")?"Mac OS":e.includes("linux")?"Linux":"Unparsed"}Object.defineProperty(r,"__esModule",{value:!0}),r.parseUASimple=function(e,r){var t=e.toLowerCase();return{browser:c(t),device:n(t),appVersion:r}};var o=/(chrome|firefox)\/([\w\.]+)/i,a=/(edge|opr)\/([\w\.]+)/i,i={chrome:"Chrome",edge:"Edge",opr:"Opera",firefox:"Firefox"};function c(e){var r=e.match(a)||e.match(o);return null==r?"Unparsed":"".concat(i[r[1]]," ").concat(r[2])}},dadahbedbh:function(e,r,t){"use strict";Object.defineProperty(r,"__esModule",{value:!0}),r.getLogUserAgent=function(e){var r,t=e.appVersion,n=e.browser,o=e.device;return r="Web/"+n,"WhatsApp/".concat(t," ").concat(r," Device/").concat(o)}},dfjdhbagei:function(e,r,t){"use strict";Object.defineProperty(r,"__esModule",{value:!0}),r.logProgressError=function(e){p(i({error:"unexpected error in progress.js",reason:String(e),stack:e.stack||""}),"progress")},r.logScriptLoadError=function(e,r){if(0===r)return;var t=a(e),n=i({error:"failed to load a js or css bundle",reason:"failed to load [".concat(t,"] on [").concat(r,"] retry"),stack:""});5===r&&p(n,"load")},r.logScriptEventualSuccess=function(e,r){var t=a(e),n=(new Date).toISOString();p("".concat(n,": [eventual success]: ").concat(t," loaded after ").concat(r," attempts in series\n").concat(n,": userAgent: ").concat(window.navigator.userAgent),"load")};var n=t("dadahbedbh"),o=t("cjighbeabh");function a(e){return e.split(".")[0].replace(/^\//,"")}function i(e){var r=e.error,t=e.reason,n=e.stack,o=(new Date).toISOString();return"".concat(o,": error: ").concat(r,"\n").concat(o,": reason for logs: ").concat(t,"\n").concat(o,": userAgent: ").concat(window.navigator.userAgent,"\n").concat(n)}var c,s="2.2017.6",u="https://crashlogs.whatsapp.net/wa_clb_data",d="1063127757113399|745146ffa34413f9dbb5469f5370b7af",f="WAUnknownID",l="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36";function p(e,r){var t=window.navigator.userAgent;if(t!==l||!e.includes("getElementsByTagName")){var a=new FormData,i=new Blob([e],{type:"text/plain"});a.append("from",function(){if(c)return c;try{(c=JSON.parse(window.localStorage.getItem(f)))&&(c=c.replace("-",""))}catch(e){}if(!c){c="unknown"+Math.floor(1e10*Math.random());try{window.localStorage.setItem(f,JSON.stringify(c))}catch(e){}}return c}()),a.append("agent",(0,n.getLogUserAgent)((0,o.parseUASimple)(t,s))),a.append("file",i,"logs.txt"),a.append("tags",r);var p=new XMLHttpRequest,g=u+"?access_token="+encodeURIComponent(d);p.open("POST",g,!0),p.send(a)}}},dgcdacjddi:function(e,r){function t(e,r){for(var t=0;t<r.length;t++){var n=r[t];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}e.exports=function(e,r,n){return r&&t(e.prototype,r),n&&t(e,n),e}},dgeiejggee:function(e,r,t){var n=Math.random()>.9,o=Math.random()>.5,a=n&&o;window.PARALLEL_FETCH_SCRIPT=n?o:null,(a?t("ecdihdgfib").default:t("bgbihbeeif").default)()},eaidjcib:function(e,r){e.exports=function(e,r){if(!(e instanceof r))throw new TypeError("Cannot call a class as a function")}},ecdihdgfib:function(e,r,t){"use strict";var n=t("cfjecfhbfg");Object.defineProperty(r,"__esModule",{value:!0}),r.default=function(){var e=document.getElementById("app");if(!e)throw"root element app not found";if(!e.dataset)throw"missing dataset annotations on app for bundles";var r=[{src:e.dataset.vendor1,size:+e.dataset.vendor1Size},{src:e.dataset.vendor2,size:+e.dataset.vendor2Size},{src:e.dataset.app,size:+e.dataset.appSize}],t=[{src:e.dataset.cssmApp,size:0},{src:e.dataset.app2,size:0}];a.default.loadScriptsWithFallbackToSeries(r,{onProgress:function(e){var r=document.getElementById("progressbar");r&&r.setAttribute("value",e.progress.toString())}}).then((function(e){return"parallel"===e.strategy?a.default.loadScriptsWithFallbackToSeries(t).then((function(e){return e})):a.default.loadInSeriesWithRetry(t,{onProgress:function(){}}).then((function(e){return e}))})).catch((function(e){throw(0,o.logProgressError)(e),e})).then((function(e){return window.Exe(Promise.resolve()),e}))};var o=t("dfjdhbagei"),a=n(t("bcceefiggd"));if(window.onerror=function(e,r,t,n,a){return(0,o.logProgressError)(a),!0},window.navigator.serviceWorker&&!window.navigator.serviceWorker.controller)try{window.navigator.serviceWorker.register("/serviceworker.js",{scope:"/"})}catch(e){}},jegfdjaci:function(e,r,t){"use strict";Object.defineProperty(r,"__esModule",{value:!0}),r.default=function(e,r){var t=[];return e.reduce((function(e,n,o,a){return e.then((function(){return r(n)})).then((function(e){return t.push(e),t}))}),Promise.resolve())}}});</script></body></html>