webpackJsonp([12],{"+L4n":function(t,a,e){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var n,i=e("bOdI"),s=e.n(i),c=(e("3Lne"),e("SSsa")),l=(e("Ny/I"),e("7Tnr")),o=(e("LlGJ"),e("Wtz3")),v=(e("JRZP"),e("LK01")),r=(e("ZuV/"),e("37Xn")),f=(e("3ab0"),e("bHMa")),_=(e("9++/"),e("QhyB")),d=(e("ibaI"),e("Ni69")),p=(e("I4j4"),e("7fQT")),u=(e("jAcA"),e("86U2")),x=(e("yIEv"),e("OIh9")),g={name:"user",components:(n={},s()(n,x.a.name,x.a),s()(n,u.a.name,u.a),s()(n,p.a.name,p.a),s()(n,d.a.name,d.a),s()(n,_.a.name,_.a),s()(n,f.a.name,f.a),s()(n,r.a.name,r.a),s()(n,v.a.name,v.a),s()(n,o.a.name,o.a),s()(n,l.a.name,l.a),s()(n,c.a.name,c.a),n),methods:{toTask:function(t){this.$router.push({name:"getTask",query:{activeIndex:t}})}}},y={render:function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",[e("van-row",{staticClass:"home-top"},[e("van-row",{staticClass:"home-top-base"},[e("van-col",{staticClass:"base-logo",attrs:{span:"6"}}),t._v(" "),e("van-col",{staticClass:"base-nick",attrs:{span:"15"}},[e("div",[t._v("18864835725")]),t._v(" "),e("div",[t._v("MR.k(青铜)")])]),t._v(" "),e("van-col",{staticStyle:{"margin-top":"15px","text-align":"end"},attrs:{span:"3"}},[e("van-icon",{staticStyle:{"font-size":"20px"},attrs:{name:"set"}})],1)],1),t._v(" "),e("van-row",{staticClass:"home-top-acc"},[e("div",{staticClass:"acc-lave"},[t._v("账户余额："),e("span",{staticStyle:{color:"#c51f1fab"}},[t._v("1.00")]),e("van-button",{staticStyle:{float:"right"},attrs:{type:"primary",size:"mini"},on:{click:function(a){return t.toOrderDetail(t.task.tasks_id)}}},[t._v("提现")])],1),t._v(" "),e("van-row",{staticClass:"acc-list"},[e("van-col",{attrs:{span:"6"}},[e("div",{staticStyle:{"text-align":"center",color:"#f1bd01","font-size":"12px"}},[t._v("1.00")]),t._v(" "),e("div",{staticStyle:{"font-size":"12px","text-align":"center"}},[t._v("任务奖励")])]),t._v(" "),e("van-col",{attrs:{span:"6"}},[e("div",{staticStyle:{"text-align":"center",color:"#f1bd01","font-size":"12px"}},[t._v("0.00")]),t._v(" "),e("div",{staticStyle:{"font-size":"12px","text-align":"center"}},[t._v("套餐提成")])]),t._v(" "),e("van-col",{attrs:{span:"6"}},[e("div",{staticStyle:{"text-align":"center",color:"#f1bd01","font-size":"12px"}},[t._v("0.00")]),t._v(" "),e("div",{staticStyle:{"font-size":"12px","text-align":"center"}},[t._v("团队收益")])]),t._v(" "),e("van-col",{attrs:{span:"6"}},[e("div",{staticStyle:{"text-align":"center",color:"#f1bd01","font-size":"12px"}},[t._v("1.00")]),t._v(" "),e("div",{staticStyle:{"font-size":"12px","text-align":"center"}},[t._v("今日收益")])])],1)],1)],1),t._v(" "),e("van-row",{staticClass:"home-top-acc",staticStyle:{margin:"20px","border-radius":"10px",background:"#f6b806",height:"100px"}},[e("van-col",{staticStyle:{color:"#ffffff"},attrs:{span:"12"},on:{click:function(a){return t.toTask(0)}}},[e("div",{staticStyle:{"text-align":"center","font-size":"12px"}},[t._v("普通任务")]),t._v(" "),e("div",{staticStyle:{"text-align":"center","font-size":"22px"}},[t._v("2/2")]),t._v(" "),e("div",{staticStyle:{"text-align":"center","font-size":"12px"}},[t._v("今日已做/今日可做")])]),t._v(" "),e("div",{staticStyle:{position:"absolute",left:"50%",width:"1px",height:"60px",background:"#ffffff",top:"20px"}}),t._v(" "),e("van-col",{staticStyle:{color:"#ffffff"},attrs:{span:"12"},on:{click:function(a){return t.toTask(1)}}},[e("div",{staticStyle:{"text-align":"center","font-size":"12px"}},[t._v("会员任务")]),t._v(" "),e("div",{staticStyle:{"text-align":"center","font-size":"22px"}},[t._v("2/2")]),t._v(" "),e("div",{staticStyle:{"text-align":"center","font-size":"12px"}},[t._v("今日已做/今日可做")])])],1),t._v(" "),e("div",{staticClass:"user_module"},[e("van-cell-group",[e("van-cell",{attrs:{icon:"shoucang",title:"提现记录",to:"/withdraw",isLink:""}}),t._v(" "),e("van-cell",{attrs:{icon:"dingwei",title:"资金明细",to:"/fundDetail",isLink:""}}),t._v(" "),e("van-cell",{attrs:{icon:"kefu",title:"我的邀请码",to:"/myInvitation",isLink:""}}),t._v(" "),e("van-cell",{attrs:{icon:"kefu",title:"我的团队",to:"/user/server",isLink:""}})],1)],1),t._v(" "),e("div",{staticClass:"user_module",staticStyle:{margin:"10px 0"}},[e("van-cell-group",[e("van-cell",{attrs:{icon:"shoucang",title:"我的任务",to:"/user/collect",isLink:""}}),t._v(" "),e("van-cell",{attrs:{icon:"dingwei",title:"开通会员",to:"/user/address",isLink:""}}),t._v(" "),e("van-cell",{attrs:{icon:"kefu",title:"联系客服",to:"/user/server",isLink:""}})],1)],1)],1)},staticRenderFns:[]};var m=e("VU/8")(g,y,!1,function(t){e("2TJR")},"data-v-522d9888",null);a.default=m.exports},"2TJR":function(t,a){}});
//# sourceMappingURL=12.cef7d8ffbe46eaed0038.js.map