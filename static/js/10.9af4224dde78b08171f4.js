webpackJsonp([10],{1468:function(e,o){},qKOq:function(e,o,t){"use strict";Object.defineProperty(o,"__esModule",{value:!0});var s,n=t("bOdI"),a=t.n(n),i=t("BD25"),r=t("lIbZ"),c=t("NK8u"),d=t("8GnF"),l={data:function(){return{counting:!1,mobile:"",code:"",isErrow:!1,password:"",passwordRepeat:""}},methods:{submitCode:function(){var e={username:this.mobile,code:this.code,password:this.password};Object(d.k)(e).then(function(e){console.log(e)})},getCode:function(){var e={mobile:this.mobile};Object(d.c)(e).then(function(e){console.log(e)})},countdownend:function(){this.counting=!1}},components:(s={},a()(s,r.a.name,r.a),a()(s,c.a.name,c.a),a()(s,"v-header",i.a),s)},u={render:function(){var e=this,o=e.$createElement,t=e._self._c||o;return t("md-field-group",{staticClass:"foget_view",staticStyle:{"margin-top":"44px"}},[t("md-field",{attrs:{icon:"mobile",placeholder:"请输入手机号"},model:{value:e.mobile,callback:function(o){e.mobile=o},expression:"mobile"}}),e._v(" "),t("md-field",{attrs:{icon:"comment",placeholder:"请输入短信验证码"},model:{value:e.code,callback:function(o){e.code=o},expression:"code"}},[t("div",{staticClass:"getCode",attrs:{slot:"rightIcon"},on:{click:e.getCode},slot:"rightIcon"},[e.counting?t("countdown",{attrs:{time:6e4},on:{end:e.countdownend},scopedSlots:e._u([{key:"default",fn:function(o){return[e._v(e._s(+o.seconds||60)+"秒后获取")]}}],null,!1,3439920001)}):t("span",[e._v("获取验证码")])],1)]),e._v(" "),t("md-field",{attrs:{icon:"lock","is-error":e.isErrow,placeholder:"请输入新密码"},model:{value:e.password,callback:function(o){e.password=o},expression:"password"}}),e._v(" "),t("md-field",{attrs:{type:"password",icon:"lock","is-error":e.isErrow,placeholder:"请再次输入密码"},model:{value:e.passwordRepeat,callback:function(o){e.passwordRepeat=o},expression:"passwordRepeat"}}),t("div",{directives:[{name:"show",rawName:"v-show",value:e.isErrow,expression:"isErrow"}],staticClass:"red"},[e._v("两次密码输入不一致")]),t("div",{staticClass:"foget_submit"},[t("van-button",{attrs:{size:"large",type:"primary"},on:{click:e.submitCode}},[e._v("重置")])],1)],1)},staticRenderFns:[]};var p=t("VU/8")(l,u,!1,function(e){t("1468")},"data-v-dded157c",null);o.default=p.exports}});
//# sourceMappingURL=10.9af4224dde78b08171f4.js.map