document.addEventListener("DOMContentLoaded",function(e){var t,n={min:0,max:200,donut:!0,gaugeWidthScale:.6,counter:!0,hideInnerShadow:!0,gaugeColor:["rgba(42, 118, 244, .1)"],levelColors:["#4c7cf5"]};function o(e,t){return Math.floor(Math.random()*(t-e+1))+e}new JustGage({id:"gg1",value:125,title:"javascript call",defaults:n}),new JustGage({id:"gg2",title:"data-attributes",defaults:n}),t=new JustGage({id:"Counter_2",value:72,min:0,max:100,donut:!0,gaugeWidthScale:.6,counter:!0,hideInnerShadow:!0,gaugeColor:["rgba(42, 118, 244, .1)"],levelColors:["#4c7cf5"]}),document.getElementById("Counter_2_refresh").addEventListener("click",function(){t.refresh(o(0,100))});var a=new JustGage({id:"Counter",value:40960,min:1024,max:1e6,gaugeWidthScale:.6,counter:!0,formatNumber:!0,gaugeColor:["rgba(42, 118, 244, .1)"],levelColors:["#4c7cf5"]});document.getElementById("Counter_refresh").addEventListener("click",function(){a.refresh(o(1024,1e6))});var l=new JustGage({id:"Animation_Events",value:45,min:0,max:100,symbol:"%",pointer:!0,gaugeColor:["rgba(42, 118, 244, .1)"],levelColors:["#4c7cf5"],pointerOptions:{toplength:-15,bottomlength:10,bottomwidth:12,color:"#ff5da0",stroke:"#ffffff",stroke_width:3,stroke_linecap:"round"},gaugeWidthScale:.6,counter:!0,onAnimationEnd:function(){console.log("animation ended");var e=document.getElementById("log");e.innerHTML=e.innerHTML+"Animation just ended.<br/>"}});document.getElementById("Animation_Events_refresh").addEventListener("click",function(){l.refresh(o(0,100))});var r=new JustGage({id:"Custom_wether",value:50,min:0,max:100,title:"Target",label:"temperature",pointer:!0,gaugeColor:["rgba(42, 118, 244, .1)"],levelColors:["#4c7cf5"],textRenderer:function(e){return e<50?"Cold":50<e?"Hot":50===e?"OK":void 0},onAnimationEnd:function(){console.log("f: onAnimationEnd()")}});document.getElementById("Custom_wether_refresh").addEventListener("click",function(){return r.refresh(o(0,100)),!1}),font_option=new JustGage({id:"font_option",title:"Font Options",value:72,min:0,minTxt:"min",max:100,maxTxt:"max",gaugeWidthScale:.6,counter:!0,gaugeColor:["rgba(42, 118, 244, .1)"],levelColors:["#4c7cf5"],titleFontColor:"red",titleFontFamily:"Georgia",titlePosition:"below",valueFontColor:"blue",valueFontFamily:"Georgia"}),document.getElementById("font_option_refresh").addEventListener("click",function(){font_option.refresh(o(0,100))});var i={label:"label",value:65,min:0,max:100,decimals:0,gaugeWidthScale:.6,pointer:!0,gaugeColor:["rgba(42, 118, 244, .1)"],levelColors:["#4c7cf5"],pointerOptions:{toplength:10,bottomlength:10,bottomwidth:2},counter:!0},u={label:"label",value:35,min:0,max:100,decimals:0,gaugeWidthScale:.6,pointer:!0,gaugeColor:["rgba(42, 118, 244, .1)"],levelColors:["#4c7cf5"],pointerOptions:{toplength:5,bottomlength:15,bottomwidth:2},counter:!0,donut:!0};new JustGage({id:"jg1",defaults:i}),new JustGage({id:"jg2",defaults:i}),new JustGage({id:"jg3",defaults:i}),new JustGage({id:"jg4",defaults:u}),new JustGage({id:"jg5",defaults:u}),new JustGage({id:"jg6",defaults:u})});