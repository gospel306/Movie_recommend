<template >
  <v-navigation-drawer
    v-model="drawer"
    width="4%"
    app
    right
    class="black"
  >
    <v-layout column justify-center text-sm-left>
      <v-flex class="ma-1"/>
      <v-flex  class="ma-2"  v-if="$store.state.login == false">
        <v-tooltip left>
          <template v-slot:activator="{ on }">
            <v-btn icon @click="goTo('login')" class="toolbartext" v-on="on">
              <v-icon large color="white" class="vic">mdi-login</v-icon>
            </v-btn>
          </template>
          <span>로그인</span>
        </v-tooltip>
      </v-flex>
      <v-flex  class="ma-2"  v-if="$store.state.login == true">
        <v-tooltip left>
          <template v-slot:activator="{ on }">
            <v-btn icon @click="logout()" class="toolbartext" v-on="on">
              <v-icon large color="white" class="vic">mdi-logout</v-icon>
            </v-btn>
          </template>
          <span>로그아웃</span>
        </v-tooltip>
      </v-flex>
      <v-flex  class="ma-2"  v-if="$store.state.login == false">
        <v-tooltip left>
          <template v-slot:activator="{ on }">
            <v-btn icon @click="goTo('signup')" class="toolbartext" v-on="on">
              <v-icon large color="white" class="vic">mdi-account-plus</v-icon>
            </v-btn>
          </template>
          <span>회원가입</span>
        </v-tooltip>
      </v-flex>
      <v-flex  class="ma-2"  v-if="$store.state.login == true && $session.get('id')=='admin'">
        <v-tooltip left>
          <template v-slot:activator="{ on }">
            <v-btn icon @click="goTo('admin')" class="toolbartext" v-on="on">
              <v-icon large color="white" class="vic">mdi-settings</v-icon>
            </v-btn>
          </template>
          <span>관리자정보</span>
        </v-tooltip>
      </v-flex>
      <v-flex  class="ma-2"  v-if="$store.state.login == true && $session.get('id')!='admin'">
        <v-tooltip left>
          <template v-slot:activator="{ on }">
            <v-btn icon @click="goTo('profile')" class="toolbartext" v-on="on">
              <v-icon large color="white" class="vic">mdi-account</v-icon>
            </v-btn>
          </template>
          <span>회원정보</span>
        </v-tooltip>
      </v-flex>
      <template v-for="i in this.$store.state.rightNavNum">
        <v-flex class="ma-2"  :key="i">
          <v-tooltip left>
            <template v-slot:activator="{ off }">
              <v-btn icon class="toolbartext" v-on="on">
                <v-icon large color="white">mdi-checkbox-blank</v-icon>
              </v-btn>
            </template>            
          </v-tooltip>
        </v-flex>
      </template>   
    </v-layout>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "RightNav",
  data(){
    return{
      drawer: null,
    }
  },
  methods: {
    goTo(path) {
      this.$router.push(path);
    },
    logout(){
      this.$store.state.login = false;
      this.$session.clear();
      this.$router.push("/");
      alert("성공적으로 로그아웃되었습니다.");
    }
  }
};
</script>

<style>
#keep .v-navigation-drawer__border {
  display: none;
}
.background{
  background: black
} 
.bt{
  margin: 11px 0px;
}
#fir{
  margin-top:20px;
}
</style>

