webpackJsonp([2],{"+B/h":function(t,e){},"+c27":function(t,e){},"/E+L":function(t,e){},"0KWt":function(t,e,i){"use strict";var n=i("o69Z"),o=i("1SJR"),s=i("V+2B"),a=Object(n.b)("tabbar"),c=a[0],r=a[1];e.a=c({mixins:[Object(o.b)("vanTabbar")],props:{route:Boolean,zIndex:[Number,String],placeholder:Boolean,activeColor:String,inactiveColor:String,value:{type:[Number,String],default:0},border:{type:Boolean,default:!0},fixed:{type:Boolean,default:!0},safeAreaInsetBottom:{type:Boolean,default:null}},data:function(){return{height:null}},computed:{fit:function(){return null!==this.safeAreaInsetBottom?this.safeAreaInsetBottom:this.fixed}},watch:{value:"setActiveItem",children:"setActiveItem"},mounted:function(){this.placeholder&&this.fixed&&(this.height=this.$refs.tabbar.getBoundingClientRect().height)},methods:{setActiveItem:function(){var t=this;this.children.forEach(function(e,i){e.active=(e.name||i)===t.value})},onChange:function(t){t!==this.value&&(this.$emit("input",t),this.$emit("change",t))},genTabbar:function(){var t;return(0,this.$createElement)("div",{ref:"tabbar",style:{zIndex:this.zIndex},class:[(t={},t[s.f]=this.border,t),r({unfit:!this.fit,fixed:this.fixed})]},[this.slots()])}},render:function(){var t=arguments[0];return this.placeholder&&this.fixed?t("div",{class:r("placeholder"),style:{height:this.height+"px"}},[this.genTabbar()]):this.genTabbar()}})},"1E9F":function(t,e,i){"use strict";var n=i("nsZj"),o=(i.n(n),i("T2s0")),s=(i.n(o),i("1H7Z")),a=(i.n(s),i("NAlg"));i.n(a)},"2Ux5":function(t,e,i){"use strict";var n=i("RfZZ"),o=i("o69Z"),s=i("n8HW"),a=i("1SJR"),c=i("+2ln"),r=i("Pen3"),l=Object(o.b)("tabbar-item"),h=l[0],u=l[1];e.a=h({mixins:[Object(a.a)("vanTabbar")],props:Object(n.a)(Object(n.a)({},s.c),{},{dot:Boolean,icon:String,name:[Number,String],info:[Number,String],badge:[Number,String],iconPrefix:String}),data:function(){return{active:!1}},computed:{routeActive:function(){var t=this.to,e=this.$route;if(t&&e){var i=Object(o.f)(t)?t:{path:t},n=i.path===e.path,s=Object(o.d)(i.name)&&i.name===e.name;return n||s}}},methods:{onClick:function(t){this.parent.onChange(this.name||this.index),this.$emit("click",t),Object(s.b)(this.$router,this)},genIcon:function(t){var e=this.$createElement,i=this.slots("icon",{active:t});return i||(this.icon?e(c.a,{attrs:{name:this.icon,classPrefix:this.iconPrefix}}):void 0)}},render:function(){var t=arguments[0],e=this.parent.route?this.routeActive:this.active,i=this.parent[e?"activeColor":"inactiveColor"];return t("div",{class:u({active:e}),style:{color:i},on:{click:this.onClick}},[t("div",{class:u("icon")},[this.genIcon(e),t(r.a,{attrs:{dot:this.dot,info:Object(o.d)(this.badge)?this.badge:this.info}})]),t("div",{class:u("text")},[this.slots("default",{active:e})])])}})},"38Ag":function(t,e){},"7ZPY":function(t,e,i){"use strict";var n=i("o69Z"),o=i("vQ9b"),s=i("RP/J"),a=i("3X7g"),c=i("joY4"),r=i("vwLT"),l=i("1SJR"),h=i("5Fm4"),u=Object(n.b)("swipe"),d=u[0],f=u[1];e.a=d({mixins:[r.a,Object(l.b)("vanSwipe"),Object(h.a)(function(t,e){t(window,"resize",this.resize,!0),t(window,"visibilitychange",this.onVisibilityChange),e?this.initialize():this.clear()})],props:{width:[Number,String],height:[Number,String],autoplay:[Number,String],vertical:Boolean,lazyRender:Boolean,indicatorColor:String,loop:{type:Boolean,default:!0},duration:{type:[Number,String],default:500},touchable:{type:Boolean,default:!0},initialSwipe:{type:[Number,String],default:0},showIndicators:{type:Boolean,default:!0},stopPropagation:{type:Boolean,default:!0}},data:function(){return{rect:null,offset:0,active:0,deltaX:0,deltaY:0,swiping:!1,computedWidth:0,computedHeight:0}},watch:{children:function(){this.initialize()},initialSwipe:function(){this.initialize()},autoplay:function(t){t>0?this.autoPlay():this.clear()}},computed:{count:function(){return this.children.length},maxCount:function(){return Math.ceil(Math.abs(this.minOffset)/this.size)},delta:function(){return this.vertical?this.deltaY:this.deltaX},size:function(){return this[this.vertical?"computedHeight":"computedWidth"]},trackSize:function(){return this.count*this.size},activeIndicator:function(){return(this.active+this.count)%this.count},isCorrectDirection:function(){var t=this.vertical?"vertical":"horizontal";return this.direction===t},trackStyle:function(){var t,e=this.vertical?"height":"width",i=this.vertical?"width":"height";return(t={})[e]=this.trackSize+"px",t[i]=this[i]?this[i]+"px":"",t.transitionDuration=(this.swiping?0:this.duration)+"ms",t.transform="translate"+(this.vertical?"Y":"X")+"("+this.offset+"px)",t},indicatorStyle:function(){return{backgroundColor:this.indicatorColor}},minOffset:function(){return(this.vertical?this.rect.height:this.rect.width)-this.size*this.count}},mounted:function(){this.bindTouchEvent(this.$refs.track)},methods:{initialize:function(t){if(void 0===t&&(t=+this.initialSwipe),this.$el&&!Object(o.a)(this.$el)){clearTimeout(this.timer);var e=this.$el.getBoundingClientRect();this.rect=e,this.swiping=!0,this.active=t,this.computedWidth=Math.round(+this.width||e.width),this.computedHeight=Math.round(+this.height||e.height),this.offset=this.getTargetOffset(t),this.children.forEach(function(t){t.offset=0}),this.autoPlay()}},resize:function(){this.initialize(this.activeIndicator)},onVisibilityChange:function(){document.hidden?this.clear():this.autoPlay()},onTouchStart:function(t){this.touchable&&(this.clear(),this.touchStartTime=Date.now(),this.touchStart(t),this.correctPosition())},onTouchMove:function(t){this.touchable&&this.swiping&&(this.touchMove(t),this.isCorrectDirection&&(Object(s.c)(t,this.stopPropagation),this.move({offset:this.delta})))},onTouchEnd:function(){if(this.touchable&&this.swiping){var t=this.size,e=this.delta,i=e/(Date.now()-this.touchStartTime);if((Math.abs(i)>.25||Math.abs(e)>t/2)&&this.isCorrectDirection){var n=this.vertical?this.offsetY:this.offsetX,o=0;o=this.loop?n>0?e>0?-1:1:0:-Math[e>0?"ceil":"floor"](e/t),this.move({pace:o,emitChange:!0})}else e&&this.move({pace:0});this.swiping=!1,this.autoPlay()}},getTargetActive:function(t){var e=this.active,i=this.count,n=this.maxCount;return t?this.loop?Object(c.b)(e+t,-1,i):Object(c.b)(e+t,0,n):e},getTargetOffset:function(t,e){void 0===e&&(e=0);var i=t*this.size;this.loop||(i=Math.min(i,-this.minOffset));var n=Math.round(e-i);return this.loop||(n=Object(c.b)(n,this.minOffset,0)),n},move:function(t){var e=t.pace,i=void 0===e?0:e,n=t.offset,o=void 0===n?0:n,s=t.emitChange,a=this.loop,c=this.count,r=this.active,l=this.children,h=this.trackSize,u=this.minOffset;if(!(c<=1)){var d=this.getTargetActive(i),f=this.getTargetOffset(d,o);if(a){if(l[0]&&f!==u){var p=f<u;l[0].offset=p?h:0}if(l[c-1]&&0!==f){var v=f>0;l[c-1].offset=v?-h:0}}this.active=d,this.offset=f,s&&d!==r&&this.$emit("change",this.activeIndicator)}},prev:function(){var t=this;this.correctPosition(),this.resetTouchStatus(),Object(a.b)(function(){t.swiping=!1,t.move({pace:-1,emitChange:!0})})},next:function(){var t=this;this.correctPosition(),this.resetTouchStatus(),Object(a.b)(function(){t.swiping=!1,t.move({pace:1,emitChange:!0})})},swipeTo:function(t,e){var i=this;void 0===e&&(e={}),this.correctPosition(),this.resetTouchStatus(),Object(a.b)(function(){var n;n=i.loop&&t===i.count?0===i.active?0:t:t%i.count,e.immediate?Object(a.b)(function(){i.swiping=!1}):i.swiping=!1,i.move({pace:n-i.active,emitChange:!0})})},correctPosition:function(){this.swiping=!0,this.active<=-1&&this.move({pace:this.count}),this.active>=this.count&&this.move({pace:-this.count})},clear:function(){clearTimeout(this.timer)},autoPlay:function(){var t=this,e=this.autoplay;e>0&&this.count>1&&(this.clear(),this.timer=setTimeout(function(){t.next(),t.autoPlay()},e))},genIndicator:function(){var t=this,e=this.$createElement,i=this.count,n=this.activeIndicator,o=this.slots("indicator");return o||(this.showIndicators&&i>1?e("div",{class:f("indicators",{vertical:this.vertical})},[Array.apply(void 0,Array(i)).map(function(i,o){return e("i",{class:f("indicator",{active:o===n}),style:o===n?t.indicatorStyle:null})})]):void 0)}},render:function(){var t=arguments[0];return t("div",{class:f()},[t("div",{ref:"track",style:this.trackStyle,class:f("track",{vertical:this.vertical})},[this.slots()]),this.genIndicator()])}})},"97dx":function(t,e){},A5M4:function(t,e){},Jqrt:function(t,e){},JsOw:function(t,e){},NAlg:function(t,e){},RgoE:function(t,e,i){"use strict";var n=i("nsZj"),o=(i.n(n),i("97dx"));i.n(o)},W0KU:function(t,e){},X6Tt:function(t,e,i){"use strict";i.d(e,"a",function(){return n});var n={inject:{vanField:{default:null}},watch:{value:function(){var t=this.vanField;t&&(t.resetValidation(),t.validateWithTrigger("onChange"))}},created:function(){var t=this.vanField;t&&!t.children&&(t.children=this)}}},ZtVa:function(t,e){},juSK:function(t,e){},"n/tq":function(t,e){},rD0v:function(t,e,i){"use strict";var n=i("RfZZ"),o=i("o69Z"),s=i("1SJR"),a=Object(o.b)("swipe-item"),c=a[0],r=a[1];e.a=c({mixins:[Object(s.a)("vanSwipe")],data:function(){return{offset:0,mounted:!1}},mounted:function(){var t=this;this.$nextTick(function(){t.mounted=!0})},computed:{style:function(){var t={},e=this.parent,i=e.size,n=e.vertical;return t[n?"height":"width"]=i+"px",this.offset&&(t.transform="translate"+(n?"Y":"X")+"("+this.offset+"px)"),t},shouldRender:function(){var t=this.index,e=this.parent,i=this.mounted;if(!e.lazyRender)return!0;if(!i)return!1;var n=e.activeIndicator,o=e.count-1;return t===n||t===(0===n?o:n-1)||t===(n===o?0:n+1)}},render:function(){return(0,arguments[0])("div",{class:r(),style:this.style,on:Object(n.a)({},this.$listeners)},[this.shouldRender&&this.slots()])}})},zKIK:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=i("bOdI"),o=i.n(n),s=(i("nsZj"),i("T2s0"),i("1H7Z"),i("+B/h"),i("o69Z")),a=i("3X7g"),c=i("+2ln"),r=Object(s.b)("notice-bar"),l=r[0],h=r[1],u=l({props:{text:String,mode:String,color:String,leftIcon:String,wrapable:Boolean,background:String,scrollable:{type:Boolean,default:null},delay:{type:[Number,String],default:1},speed:{type:[Number,String],default:50}},data:function(){return{show:!0,offset:0,duration:0,wrapWidth:0,contentWidth:0}},watch:{scrollable:"start",text:{handler:"start",immediate:!0}},activated:function(){this.start()},methods:{onClickIcon:function(t){"closeable"===this.mode&&(this.show=!1,this.$emit("close",t))},onTransitionEnd:function(){var t=this;this.offset=this.wrapWidth,this.duration=0,setTimeout(function(){t.offset=-t.contentWidth,t.duration=(t.contentWidth+t.wrapWidth)/t.speed,t.$emit("replay")},100)},reset:function(){this.offset=0,this.duration=0,this.wrapWidth=0,this.contentWidth=0},start:function(){var t=this,e=Object(s.d)(this.delay)?1e3*this.delay:0;this.reset(),setTimeout(function(){var e=t.$refs,i=e.wrap,n=e.content;if(i&&n&&!1!==t.scrollable){var o=i.getBoundingClientRect().width,s=n.getBoundingClientRect().width;(t.scrollable||s>o)&&Object(a.b)(function(){t.offset=-s,t.duration=s/t.speed,t.wrapWidth=o,t.contentWidth=s})}},e)}},render:function(){var t,e=this,i=arguments[0],n=this.slots,o=this.mode,s=this.leftIcon,a=this.onClickIcon,r={color:this.color,background:this.background},l={transform:this.offset?"translateX("+this.offset+"px)":"",transitionDuration:this.duration+"s"};return i("div",{attrs:{role:"alert"},directives:[{name:"show",value:this.show}],class:h({wrapable:this.wrapable}),style:r,on:{click:function(t){e.$emit("click",t)}}},[(t=n("left-icon"),t||(s?i(c.a,{class:h("left-icon"),attrs:{name:s}}):void 0)),i("div",{ref:"wrap",class:h("wrap"),attrs:{role:"marquee"}},[i("div",{ref:"content",class:[h("content"),{"van-ellipsis":!1===this.scrollable&&!this.wrapable}],style:l,on:{transitionend:this.onTransitionEnd}},[this.slots()||this.text])]),function(){var t,e=n("right-icon");return e||("closeable"===o?t="cross":"link"===o&&(t="arrow"),t?i(c.a,{class:h("right-icon"),attrs:{name:t},on:{click:a}}):void 0)}()])}}),d=(i("juSK"),i("RfZZ")),f=i("V+2B"),p=i("n8HW"),v=i("1SJR"),b=i("Pen3"),g=Object(s.b)("grid-item"),m=g[0],y=g[1],S=m({mixins:[Object(v.a)("vanGrid")],props:Object(d.a)(Object(d.a)({},p.c),{},{dot:Boolean,text:String,icon:String,iconPrefix:String,info:[Number,String],badge:[Number,String]}),computed:{style:function(){var t=this.parent,e=t.square,i=t.gutter,n=t.columnNum,o=100/n+"%",a={flexBasis:o};if(e)a.paddingTop=o;else if(i){var c=Object(s.a)(i);a.paddingRight=c,this.index>=n&&(a.marginTop=c)}return a},contentStyle:function(){var t=this.parent,e=t.square,i=t.gutter;if(e&&i){var n=Object(s.a)(i);return{right:n,bottom:n,height:"auto"}}}},methods:{onClick:function(t){this.$emit("click",t),Object(p.b)(this.$router,this)},genIcon:function(){var t=this.$createElement,e=this.slots("icon"),i=Object(s.d)(this.badge)?this.badge:this.info;return e?t("div",{class:y("icon-wrapper")},[e,t(b.a,{attrs:{dot:this.dot,info:i}})]):this.icon?t(c.a,{attrs:{name:this.icon,dot:this.dot,info:i,size:this.parent.iconSize,classPrefix:this.iconPrefix},class:y("icon")}):void 0},getText:function(){var t=this.$createElement,e=this.slots("text");return e||(this.text?t("span",{class:y("text")},[this.text]):void 0)},genContent:function(){var t=this.slots();return t||[this.genIcon(),this.getText()]}},render:function(){var t,e=arguments[0],i=this.parent,n=i.center,o=i.border,s=i.square,a=i.gutter,c=i.direction,r=i.clickable;return e("div",{class:[y({square:s})],style:this.style},[e("div",{style:this.contentStyle,attrs:{role:r?"button":null,tabindex:r?0:null},class:[y("content",[c,{center:n,square:s,clickable:r,surround:o&&a}]),(t={},t[f.a]=o,t)],on:{click:this.onClick}},[this.genContent()])])}}),x=(i("/E+L"),Object(s.b)("grid")),w=x[0],C=x[1],k=w({mixins:[Object(v.b)("vanGrid")],props:{square:Boolean,gutter:[Number,String],iconSize:[Number,String],direction:String,clickable:Boolean,columnNum:{type:[Number,String],default:4},center:{type:Boolean,default:!0},border:{type:Boolean,default:!0}},computed:{style:function(){var t=this.gutter;if(t)return{paddingLeft:Object(s.a)(t)}}},render:function(){var t;return(0,arguments[0])("div",{style:this.style,class:[C(),(t={},t[f.e]=this.border&&!this.gutter,t)]},[this.slots()])}}),O=(i("3ab0"),i("bHMa")),T=(i("1E9F"),i("2Ux5")),j=(i("RgoE"),i("0KWt")),B=(i("W0KU"),i("rD0v")),$=(i("JsOw"),i("7ZPY")),I=(i("9++/"),i("QhyB")),z=(i("I4j4"),i("7fQT")),_=(i("qpP9"),i("px3J"),i("n/tq"),i("AA6R")),P=i.n(_),E=i("rhik"),A=i("RP/J"),R=i("0zAV"),D=Object(s.b)("search"),N=D[0],M=D[1],Z=D[2];function W(t,e,i,n){var o={attrs:n.data.attrs,on:Object(d.a)(Object(d.a)({},n.listeners),{},{keypress:function(t){13===t.keyCode&&(Object(A.c)(t),Object(E.a)(n,"search",e.value)),Object(E.a)(n,"keypress",t)}})},s=Object(E.b)(n);return s.attrs=void 0,t("div",P()([{class:M({"show-action":e.showAction}),style:{background:e.background}},s]),[null==i.left?void 0:i.left(),t("div",{class:M("content",e.shape)},[function(){if(i.label||e.label)return t("div",{class:M("label")},[i.label?i.label():e.label])}(),t(R.a,P()([{attrs:{type:"search",border:!1,value:e.value,leftIcon:e.leftIcon,rightIcon:e.rightIcon,clearable:e.clearable},scopedSlots:{"left-icon":i["left-icon"],"right-icon":i["right-icon"]}},o]))]),function(){if(e.showAction)return t("div",{class:M("action"),attrs:{role:"button",tabindex:"0"},on:{click:function(){i.action||(Object(E.a)(n,"input",""),Object(E.a)(n,"cancel"))}}},[i.action?i.action():e.actionText||Z("cancel")])}()])}W.props={value:String,label:String,rightIcon:String,actionText:String,showAction:Boolean,background:String,shape:{type:String,default:"square"},clearable:{type:Boolean,default:!0},leftIcon:{type:String,default:"search"}};var q,L,J,V,F=N(W),H=(i("+c27"),i("A5M4"),i("WpgC"),i("3IMD"),i("6gXq"),i("S6Ip"),i("bFPQ"),i("ZtVa"),i("OIh9")),X=i("86U2"),Y=i("SSsa"),K=i("YNA3"),U=i("X6Tt"),Q=Object(s.b)("checkbox"),G=Q[0],tt=Q[1],et=G({mixins:[(q={bem:tt,role:"checkbox",parent:"vanCheckbox"},L=q.parent,J=q.bem,V=q.role,{mixins:[Object(v.a)(L),U.a],props:{name:null,value:null,disabled:Boolean,iconSize:[Number,String],checkedColor:String,labelPosition:String,labelDisabled:Boolean,shape:{type:String,default:"round"},bindGroup:{type:Boolean,default:!0}},computed:{disableBindRelation:function(){return!this.bindGroup},isDisabled:function(){return this.parent&&this.parent.disabled||this.disabled},direction:function(){return this.parent&&this.parent.direction||null},iconStyle:function(){var t=this.checkedColor||this.parent&&this.parent.checkedColor;if(t&&this.checked&&!this.isDisabled)return{borderColor:t,backgroundColor:t}},tabindex:function(){return this.isDisabled||"radio"===V&&!this.checked?-1:0}},methods:{onClick:function(t){var e=this,i=t.target,n=this.$refs.icon,o=n===i||n.contains(i);this.isDisabled||!o&&this.labelDisabled?this.$emit("click",t):(this.toggle(),setTimeout(function(){e.$emit("click",t)}))},genIcon:function(){var t=this.$createElement,e=this.checked,i=this.iconSize||this.parent&&this.parent.iconSize;return t("div",{ref:"icon",class:J("icon",[this.shape,{disabled:this.isDisabled,checked:e}]),style:{fontSize:Object(s.a)(i)}},[this.slots("icon",{checked:e})||t(c.a,{attrs:{name:"success"},style:this.iconStyle})])},genLabel:function(){var t=this.$createElement,e=this.slots();if(e)return t("span",{class:J("label",[this.labelPosition,{disabled:this.isDisabled}])},[e])}},render:function(){var t=arguments[0],e=[this.genIcon()];return"left"===this.labelPosition?e.unshift(this.genLabel()):e.push(this.genLabel()),t("div",{attrs:{role:V,tabindex:this.tabindex,"aria-checked":String(this.checked)},class:J([{disabled:this.isDisabled,"label-disabled":this.labelDisabled},this.direction]),on:{click:this.onClick}},[e])}})],computed:{checked:{get:function(){return this.parent?-1!==this.parent.value.indexOf(this.name):this.value},set:function(t){this.parent?this.setParentValue(t):this.$emit("input",t)}}},watch:{value:function(t){this.$emit("change",t)}},methods:{toggle:function(t){var e=this;void 0===t&&(t=!this.checked),clearTimeout(this.toggleTask),this.toggleTask=setTimeout(function(){e.checked=t})},setParentValue:function(t){var e=this.parent,i=e.value.slice();if(t){if(e.max&&i.length>=e.max)return;-1===i.indexOf(this.name)&&(i.push(this.name),e.$emit("input",i))}else{var n=i.indexOf(this.name);-1!==n&&(i.splice(n,1),e.$emit("input",i))}}}}),it=Object(s.b)("coupon"),nt=it[0],ot=it[1],st=it[2];function at(t){var e=new Date(1e3*t);return e.getFullYear()+"."+Object(K.b)(e.getMonth()+1)+"."+Object(K.b)(e.getDate())}function ct(t){return(t/100).toFixed(t%100==0?0:t%10==0?1:2)}var rt=nt({props:{coupon:Object,chosen:Boolean,disabled:Boolean,currency:{type:String,default:"¥"}},computed:{validPeriod:function(){var t=this.coupon,e=t.startAt,i=t.endAt;return at(e)+" - "+at(i)},faceAmount:function(){var t,e=this.coupon;if(e.valueDesc)return e.valueDesc+"<span>"+(e.unitDesc||"")+"</span>";if(e.denominations){var i=ct(e.denominations);return"<span>"+this.currency+"</span> "+i}return e.discount?st("discount",((t=e.discount)/10).toFixed(t%10==0?0:1)):""},conditionMessage:function(){var t=ct(this.coupon.originCondition);return"0"===t?st("unlimited"):st("condition",t)}},render:function(){var t=arguments[0],e=this.coupon,i=this.disabled,n=i&&e.reason||e.description;return t("div",{class:ot({disabled:i})},[t("div",{class:ot("content")},[t("div",{class:ot("head")},[t("h2",{class:ot("amount"),domProps:{innerHTML:this.faceAmount}}),t("p",{class:ot("condition")},[this.coupon.condition||this.conditionMessage])]),t("div",{class:ot("body")},[t("p",{class:ot("name")},[e.name]),t("p",{class:ot("valid")},[this.validPeriod]),!this.disabled&&t(et,{attrs:{size:18,value:this.chosen,checkedColor:f.h},class:ot("corner")})])]),n&&t("p",{class:ot("description")},[n])])}}),lt=Object(s.b)("coupon-list"),ht=lt[0],ut=lt[1],dt=lt[2],ft=ht({model:{prop:"code"},props:{code:String,closeButtonText:String,inputPlaceholder:String,enabledTitle:String,disabledTitle:String,exchangeButtonText:String,exchangeButtonLoading:Boolean,exchangeButtonDisabled:Boolean,exchangeMinLength:{type:Number,default:1},chosenCoupon:{type:Number,default:-1},coupons:{type:Array,default:function(){return[]}},disabledCoupons:{type:Array,default:function(){return[]}},displayedCouponIndex:{type:Number,default:-1},showExchangeBar:{type:Boolean,default:!0},showCloseButton:{type:Boolean,default:!0},showCount:{type:Boolean,default:!0},currency:{type:String,default:"¥"},emptyImage:{type:String,default:"https://img.yzcdn.cn/vant/coupon-empty.png"}},data:function(){return{tab:0,winHeight:window.innerHeight,currentCode:this.code||""}},computed:{buttonDisabled:function(){return!this.exchangeButtonLoading&&(this.exchangeButtonDisabled||!this.currentCode||this.currentCode.length<this.exchangeMinLength)},listStyle:function(){return{height:this.winHeight-(this.showExchangeBar?140:94)+"px"}}},watch:{code:function(t){this.currentCode=t},currentCode:function(t){this.$emit("input",t)},displayedCouponIndex:"scrollToShowCoupon"},mounted:function(){this.scrollToShowCoupon(this.displayedCouponIndex)},methods:{onClickExchangeButton:function(){this.$emit("exchange",this.currentCode),this.code||(this.currentCode="")},scrollToShowCoupon:function(t){var e=this;-1!==t&&this.$nextTick(function(){var i=e.$refs,n=i.card,o=i.list;o&&n&&n[t]&&(o.scrollTop=n[t].$el.offsetTop-100)})},genEmpty:function(){var t=this.$createElement;return t("div",{class:ut("empty")},[t("img",{attrs:{src:this.emptyImage}}),t("p",[dt("empty")])])},genExchangeButton:function(){return(0,this.$createElement)(Y.a,{attrs:{plain:!0,type:"danger",text:this.exchangeButtonText||dt("exchange"),loading:this.exchangeButtonLoading,disabled:this.buttonDisabled},class:ut("exchange"),on:{click:this.onClickExchangeButton}})}},render:function(){var t=this,e=arguments[0],i=this.coupons,n=this.disabledCoupons,o=this.showCount?" ("+i.length+")":"",s=(this.enabledTitle||dt("enable"))+o,a=this.showCount?" ("+n.length+")":"",c=(this.disabledTitle||dt("disabled"))+a,r=this.showExchangeBar&&e("div",{class:ut("exchange-bar")},[e(R.a,{attrs:{clearable:!0,border:!1,placeholder:this.inputPlaceholder||dt("placeholder"),maxlength:"20"},class:ut("field"),model:{value:t.currentCode,callback:function(e){t.currentCode=e}}}),this.genExchangeButton()]),l=function(e){return function(){return t.$emit("change",e)}},h=e(H.a,{attrs:{title:s}},[e("div",{class:ut("list",{"with-bottom":this.showCloseButton}),style:this.listStyle},[i.map(function(i,n){return e(rt,{ref:"card",key:i.id,attrs:{coupon:i,currency:t.currency,chosen:n===t.chosenCoupon},nativeOn:{click:l(n)}})}),!i.length&&this.genEmpty()])]),u=e(H.a,{attrs:{title:c}},[e("div",{class:ut("list",{"with-bottom":this.showCloseButton}),style:this.listStyle},[n.map(function(i){return e(rt,{attrs:{disabled:!0,coupon:i,currency:t.currency},key:i.id})}),!n.length&&this.genEmpty()])]);return e("div",{class:ut()},[r,e(X.a,{class:ut("tab"),attrs:{border:!1},model:{value:t.tab,callback:function(e){t.tab=e}}},[h,u]),e("div",{class:ut("bottom")},[e(Y.a,{directives:[{name:"show",value:this.showCloseButton}],attrs:{round:!0,type:"danger",block:!0,text:this.closeButtonText||dt("close")},class:ut("close"),on:{click:l(-1)}})])])}}),pt=(i("Jqrt"),i("1fWZ")),vt=Object(s.b)("coupon-cell"),bt=vt[0],gt=vt[1],mt=vt[2];function yt(t,e,i,n){var o=e.coupons[+e.chosenCoupon]?"van-coupon-cell--selected":"",s=function(t){var e=t.coupons,i=t.chosenCoupon,n=t.currency,o=e[+i];return o?"-"+n+((o.value||o.denominations||0)/100).toFixed(2):0===e.length?mt("tips"):mt("count",e.length)}(e);return t(pt.a,P()([{class:gt(),attrs:{value:s,title:e.title||mt("title"),border:e.border,isLink:e.editable,valueClass:o}},Object(E.b)(n,!0)]))}yt.model={prop:"chosenCoupon"},yt.props={title:String,coupons:{type:Array,default:function(){return[]}},currency:{type:String,default:"¥"},border:{type:Boolean,default:!0},editable:{type:Boolean,default:!0},chosenCoupon:{type:[Number,String],default:-1}};var St,xt=bt(yt),wt=(i("eqfM"),i("/QYm")),Ct=(i("ibaI"),i("Ni69")),kt=(i("JRZP"),i("LK01")),Ot=(i("ZuV/"),i("37Xn")),Tt=i("M4fF"),jt={name:"home",mixins:[{data:function(){return{scrollTop:0}},mounted:function(){var t=this;t.$el.addEventListener("scroll",Object(Tt.debounce)(function(){t.scrollTop=t.$el.scrollTop},50))},activated:function(){this.$el.scrollTop=this.scrollTop}}],data:function(){return{shopInfos:[],isLoading:!1}},created:function(){this.initViews(),this.shopInfos=[{banner:[{url:"../../assets/images/head1.png"}]}]},methods:{changeTabbar:function(t){},initViews:function(){},toTask:function(t){this.$router.push({name:"getTask",query:{activeIndex:t}})}},components:(St={},o()(St,Ot.a.name,Ot.a),o()(St,kt.a.name,kt.a),o()(St,Ct.a.name,Ct.a),o()(St,wt.a.name,wt.a),o()(St,xt.name,xt),o()(St,ft.name,ft),o()(St,F.name,F),o()(St,z.a.name,z.a),o()(St,I.a.name,I.a),o()(St,$.a.name,$.a),o()(St,B.a.name,B.a),o()(St,j.a.name,j.a),o()(St,T.a.name,T.a),o()(St,O.a.name,O.a),o()(St,k.name,k),o()(St,S.name,S),o()(St,u.name,u),St)},Bt={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"tab_home"},[i("van-notice-bar",{attrs:{"left-icon":"laba",text:"恭喜 花不败 在10分钟前提现100.00元 恭喜 未来在哪里 在20分钟前提现650.00元 恭喜 敢问路在何方 在12分钟前提现8000.00元。"}}),t._v(" "),i("van-swipe",{attrs:{autoplay:3e3,"indicator-color":"white"}},[i("van-swipe-item",[i("div",{staticClass:"bg"},[i("marquee",{staticStyle:{color:"#ffffff"},attrs:{direction:"left",behavior:"scroll",scrollamount:"10",scrolldelay:"0",loop:"-1",hspace:"10",vspace:"10"}})],1)])],1),t._v(" "),i("van-row",{staticClass:"order_status"},[i("van-col",{attrs:{span:"6"}},[i("div",{staticClass:"order_status_icon",staticStyle:{background:"#f55315",color:"#ffffff"},on:{click:function(e){return t.$router.push({path:"/news"})}}},[i("van-icon",{staticClass:"iconfont icon-xinwen"})],1),t._v(" "),i("div",[t._v("通知公告")])]),t._v(" "),i("van-col",{attrs:{span:"6"}},[i("div",{staticClass:"order_status_icon",staticStyle:{background:"#f53952",color:"#ffffff"},on:{click:function(e){return t.$router.push({path:"/user/order/list/2"})}}},[i("van-icon",{staticClass:"iconfont icon-zhinanzhen"})],1),t._v(" "),i("div",[t._v("新手指南")])]),t._v(" "),i("van-col",{attrs:{span:"6"},on:{click:function(e){return t.$router.push({path:"/myInvitation"})}}},[i("div",{staticClass:"order_status_icon",staticStyle:{background:"#f59a08",color:"#ffffff"},on:{click:function(e){return t.$router.push({path:"/user/order/list/3"})}}},[i("van-icon",{staticClass:"iconfont icon-yqhy"})],1),t._v(" "),i("div",[t._v("邀请好友")])]),t._v(" "),i("van-col",{attrs:{span:"6"}},[i("div",{staticClass:"order_status_icon",staticStyle:{background:"#db3d3c",color:"#ffffff"},on:{click:function(e){return t.$router.push({path:"/user/order/list/4"})}}},[i("van-icon",{staticClass:"iconfont icon-ziyuan"})],1),t._v(" "),i("div",[t._v("开通会员")])])],1),t._v(" "),i("van-row",{staticClass:"taskRow"},[i("van-col",{attrs:{span:"12"}},[i("div",{staticClass:"order_status_icon",staticStyle:{background:"#2ee0f5",color:"#ffffff"},on:{click:function(e){return t.toTask(0)}}},[i("van-icon",{staticClass:"iconfont icon-chepai",staticStyle:{"font-size":"20px"}}),t._v(" 普通任务\n      ")],1)]),t._v(" "),i("van-col",{attrs:{span:"12"}},[i("div",{staticClass:"order_status_icon",staticStyle:{background:"#ff6ca5",color:"#ffffff"},on:{click:function(e){return t.toTask(1)}}},[i("van-icon",{staticClass:"iconfont icon-feiji",staticStyle:{"font-size":"20px"}}),t._v(" 会员任务\n      ")],1)])],1),t._v(" "),i("van-row",{staticClass:"taskRow",staticStyle:{background:"#5c85fb",color:"#ffffff"}},[i("van-col",{attrs:{span:"6"}},[i("van-icon",{staticClass:"iconfont icon-ziyuan",staticStyle:{"font-size":"25px"}})],1),t._v(" "),i("van-col",{staticStyle:{"text-align":"left"},attrs:{span:"18"}},[t._v("今日任务数: 518000")])],1),t._v(" "),i("van-row",{staticClass:"taskRow",staticStyle:{background:"#0ed4c5",color:"#ffffff"}},[i("van-col",{attrs:{span:"6"}},[i("van-icon",{staticClass:"iconfont icon-ziyuan",staticStyle:{"font-size":"25px"}})],1),t._v(" "),i("van-col",{staticStyle:{"text-align":"left"},attrs:{span:"18"}},[t._v("今日用户数: 52756")])],1),t._v(" "),i("van-row",{staticClass:"taskRow",staticStyle:{background:"#ff655b",color:"#ffffff"}},[i("van-col",{attrs:{span:"6"}},[i("van-icon",{staticClass:"iconfont icon-ziyuan",staticStyle:{"font-size":"25px"}})],1),t._v(" "),i("van-col",{staticStyle:{"text-align":"left"},attrs:{span:"18"}},[t._v("今日已完成: 2865589")])],1),t._v(" "),i("van-row",{staticClass:"taskRow",staticStyle:{background:"#ffa72d",color:"#ffffff"}},[i("van-col",{attrs:{span:"6"}},[i("van-icon",{staticClass:"iconfont icon-ziyuan",staticStyle:{"font-size":"25px"}})],1),t._v(" "),i("van-col",{staticStyle:{"text-align":"left"},attrs:{span:"18"}},[t._v("今日排行榜: 3")])],1)],1)},staticRenderFns:[]};var $t=i("VU/8")(jt,Bt,!1,function(t){i("38Ag")},"data-v-78b39854",null);e.default=$t.exports}});
//# sourceMappingURL=2.11a79fa93657cf6cd013.js.map