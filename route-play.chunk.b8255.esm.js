(window.webpackJsonp=window.webpackJsonp||[]).push([[4],{F2LE:function(e,n,t){"use strict";function r(){return r=Object.assign||function(e){for(var n=1;n<arguments.length;n++){var t=arguments[n];for(var r in t)Object.prototype.hasOwnProperty.call(t,r)&&(e[r]=t[r])}return e},r.apply(this,arguments)}function o(e,n){if(null==e)return{};var t,r,o=function(e,n){if(null==e)return{};var t,r,o={},a=Object.keys(e);for(r=0;r<a.length;r++)n.indexOf(t=a[r])>=0||(o[t]=e[t]);return o}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)n.indexOf(t=a[r])>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(o[t]=e[t])}return o}t.r(n);var a=t("hosL"),i=t("Hrl7"),s=t("QRet");const c=["getContext","init","ready","draw","onResize","framesPerSecond"],l={alpha:!1,depth:!1,preserveDrawingBuffer:!0};var u=e=>{const{getContext:n,init:t,ready:i,draw:u,onResize:d,framesPerSecond:f}=e,m=o(e,c),w=Object(a.createRef)(),v=f?1e3/f:void 0;return Object(s.d)((()=>{const e=w.current;let r,o=!1,a=-1;const s=n?n(e):e.getContext("webgl2",l),c=()=>{s.canvas.width=window.innerWidth,s.canvas.height=window.innerHeight,d&&d(s)};window.addEventListener("resize",c),c();const f=()=>{o=!0};window.addEventListener("blur",f);const m=()=>{o=!1};window.addEventListener("focus",m);const g=()=>{document.fullscreenElement||e.requestFullscreen().catch((e=>{console.log("No full!",e)}))};window.addEventListener("click",g),t&&t(s);const h=()=>{o?setTimeout(h,128):(a++,r=v?window.setTimeout(h,v):window.requestAnimationFrame(h),u(s,a))},_=()=>{setTimeout(h,0)};return void 0===i?_():i(_),()=>{v?window.clearTimeout(r):window.cancelAnimationFrame(r),window.removeEventListener("resize",c),window.removeEventListener("blur",f),window.removeEventListener("focus",m),window.removeEventListener("click",g)}}),[n,t,i,u,d,w,v]),Object(a.h)("canvas",r({ref:w},m))},d="canvas_frame__v+aHP";const f=(e,n,t)=>{const r=e.createShader(n);if(!r)throw"Missing shader";if(e.shaderSource(r,t),e.compileShader(r),!e.getShaderParameter(r,e.COMPILE_STATUS))throw e.getShaderInfoLog(r);return r};n.default=()=>{let e,n,t,r;const o=[0,0],s=[1,1];let c=1;const l=a=>{c=Math.sqrt(a.canvas.width**2+a.canvas.height**2),o[0]=-a.canvas.width/2,o[1]=-a.canvas.height/2,s[0]=s[1]=2/c,e=(e=>{const n=e.createProgram();if(!n)throw"Missing program";const t=f(e,e.FRAGMENT_SHADER,"#version 300 es\nprecision lowp float;\nuniform float u_time;\nuniform vec2 u_translate;\nuniform vec2 u_scale;\nout vec4 fragmentColor;\n\nvoid main() {\n  float m_0 = ( gl_FragCoord.x + u_translate.x ) * u_scale.x;\n  float m_1 = ( gl_FragCoord.y + u_translate.y ) * u_scale.y;\n  float radiusSquared = pow(sin(u_time/60.0), 2.0);\n  bool inside = m_0*m_0 + m_1*m_1 < radiusSquared;\n  fragmentColor.r = fragmentColor.b = inside ? 0.5 : 0.0;\n}\n");e.attachShader(n,t);const r=f(e,e.VERTEX_SHADER,"#version 300 es\nin vec2 a_position;\nin vec4 a_color;\nout vec4 v_color;\n\nvoid main(void) {\n  gl_Position = vec4(a_position, 0.0, 1.0);\n  v_color = a_color;\n}\n");var o;if(e.attachShader(n,r),e.linkProgram(n),!e.getProgramParameter(n,e.LINK_STATUS))throw null!==(o=e.getProgramInfoLog(n))&&void 0!==o?o:"Error from getProgramParameter";return e.useProgram(n),n})(a),((e,o)=>{const a=e.getAttribLocation(o,"a_position"),i=new Float32Array([1,1,0,-1,1,0,1,-1,0,-1,-1,0]),s=e.createBuffer();e.bindBuffer(e.ARRAY_BUFFER,s),e.bufferData(e.ARRAY_BUFFER,i,e.STATIC_DRAW),e.vertexAttribPointer(a,3,e.FLOAT,!1,0,0),e.bindBuffer(e.ARRAY_BUFFER,null),e.enableVertexAttribArray(a),n=e.getUniformLocation(o,"u_time"),t=e.getUniformLocation(o,"u_translate"),r=e.getUniformLocation(o,"u_scale")})(a,e)};return Object(a.h)("section",{class:d},Object(a.h)(i.a,{title:"Play"}),Object(a.h)(u,{init:l,onResize:e=>{e.viewport(0,0,e.canvas.width,e.canvas.height),e.clear(e.COLOR_BUFFER_BIT),l(e)},draw:(e,a)=>{e.uniform1f(n,a),e.uniform2f(t,o[0],o[1]),e.uniform2f(r,s[0],s[1]),e.drawArrays(e.TRIANGLE_STRIP,0,4)}}))}}}]);
//# sourceMappingURL=route-play.chunk.b8255.esm.js.map