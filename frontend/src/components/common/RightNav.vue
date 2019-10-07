<template >
  <v-navigation-drawer
    v-model="drawer"
    width="3%"
    app
    right
    class="black"
  >
    <v-layout column justify-center >
      <v-flex id="fir" class="bt" text-sm-left v-if="$store.state.login == false">
        <v-icon color="white" @click="goTo('login')" >mdi-login</v-icon>
      </v-flex>
      <v-flex class="bt" text-sm-left v-if="$store.state.login == true">
        <v-icon color="white" @click="logout()">mdi-logout</v-icon>
      </v-flex>
      <v-flex class="bt" text-sm-left v-if="$store.state.login == false">
        <v-icon color="white" @click="goTo('signup')">mdi-account-plus</v-icon>
      </v-flex>
      <v-flex class="bt" text-sm-left v-if="$store.state.login == true && $session.get('id')=='admin'">
        <v-icon color="white" @click="goTo('signup')">mdi-settings</v-icon>
      </v-flex>
      <v-flex class="bt" text-sm-left v-if="$store.state.login == true && $session.get('id')!='admin'">
        <v-icon color="white" @click="goTo('profile')">mdi-account</v-icon>
      </v-flex>
      <template v-for="i in this.$store.state.rightNavNum">
        <v-flex class="bt" text-sm-left :key="i">
          <v-icon color="white">mdi-checkbox-blank</v-icon>
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

