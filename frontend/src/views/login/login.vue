<template>
  <div class="login">
    <div class="store_header">
      <div class="store_avatar">
        <img src="../../assets/images/avatar_default.png" alt="头像" width="55" height="55">
      </div>
      <div class="store_name">赞多多</div>
    </div>

    <md-field-group>
      <md-field
        v-model="account"
        icon="mobile"
        placeholder="请输入手机号"
        right-icon="clear-full"
        name="user"
        data-vv-as="帐号"
        @right-click="clearText"
      />

      <md-field
        v-model="password"
        icon="lock"
        placeholder="请输入密码"
        :type="visiblePass ? 'text' : 'password'"
        :right-icon="visiblePass ? 'eye-open' : 'eye-close'"
        data-vv-as="密码"
        name="password"
        @right-click="visiblePass = !visiblePass"
      />

      <div class="clearfix">
        <div class="float-l">
          <router-link to="/login/register"><span style="color: #f55315;">免费注册</span></router-link>
        </div>
        <div class="float-r">
          <router-link to="/login/forget"><span style="color: #f55315;">忘记密码?</span></router-link>
        </div>
      </div>

      <van-button size="large" type="primary" :loading="isLogining" @click="loginSubmit">登录</van-button>
    </md-field-group>


    <div class="text-desc text-center bottom_positon">技术支持: 赞多多</div>

  </div>
</template>

<script>
import field from '@/components/field/'
import fieldGroup from '@/components/field-group/'

import { authLoginByAccount } from '@/api/loginapi'
import { setLocalStorage } from '@/utils/local-storage'
import { emailReg, mobileReg } from '@/utils/validate'
import { Toast } from 'vant'


export default {
  name: 'login-request',
  components: {
    [field.name]: field,
    [fieldGroup.name]: fieldGroup,
    Toast
  },
  data () {
    return {
      account: '',
      password: '',
      visiblePass: false,
      isLogining: false,
      userInfo: {}
    }
  },
  methods: {
    clearText () {
      this.account = ''
    },
    goBack () {
      this.$router.back(-1)
    },
    validate () {

    },

    login () {
      // let loginData = {
      //   username: this.account,
      //   password: this.password
      // }
      let loginData = this.getLoginData()
      authLoginByAccount(loginData).then(res => {
        // this.userInfo = res.data.data.userInfo
        setLocalStorage({
          Authorization: res.data.token,
          username: this.account
          // avatar: this.userInfo.avatarUrl,
          // nickName: this.userInfo.nickName
        })
        console.log(res)
        this.routerRedirect()
      // }).catch(error => {
      //   console.log(error)
      //   Toast.fail(error)
      })
    },

    loginSubmit () {
      this.isLogining = true
      try {
        this.validate()
        this.login()
        this.isLogining = false
      } catch (err) {
        console.log(err.message)
        this.isLogining = false
      }
    },

    routerRedirect () {
      // const { query } = this.$route;
      // this.$router.replace({
      //   name: query.redirect || 'home',
      //   query: query
      // });
      window.location = '#/user/'
    },

    getLoginData () {
      const password = this.password
      // const account = this.getUserType(this.account)
      return {
        // [account]: this.account,
        username: this.account,
        password: password
      }
    },

    getUserType (account) {
      const accountType = mobileReg.test(account)
        ? 'mobile'
        : emailReg.test(account)
          ? 'email'
          : 'username'
      return accountType
    }
  }
}
</script>


<style lang="scss" scoped>
  @import '../../assets/scss/mixin';
  .login {
    position: relative;
    background-color: #fff;
  }
  .store_header {
    text-align: center;
    padding: 30px 0;
    .store_avatar img {
      border-radius: 50%;
    }
    .store_name {
      padding-top: 5px;
      font-size: 16px;
    }
  }
  .register {
    padding-top: 40px;
    color: gray;
    a {
      color: gray;
    }
    > div {
      width: 50%;
      box-sizing: border-box;
      padding: 0 20px;
    }
    .connect {
      @include one-border(right);
      text-align: right;
    }
  }
  .bottom_positon {
    position: absolute;
    bottom: 30px;
    width: 100%;
  }
</style>
