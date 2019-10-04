<template >
  <v-navigation-drawer
    v-model="drawer"
    width="4%"
    app
    right
    class="black"
  >
    <v-list>
      <v-list-item @click="goTo('login')" v-if="$store.state.login == false">
        <v-list-item-action>
          <v-icon color="white">mdi-login</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title class="subtitle-2 font-weight-bold white--text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item @click="logout()" v-if="$store.state.login == true">
        <v-list-item-action>
          <v-icon color="white">mdi-logout</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title class="subtitle-2 font-weight-bold white--text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item @click="goTo('signup')" v-if="$store.state.login == false">
        <v-list-item-action>
          <v-icon color="white">mdi-account-plus</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title class="subtitle-2 font-weight-bold white--text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item @click="goTo('admin')" v-if="$store.state.login == true && $session.get('id')=='admin'">
        <v-list-item-action>
          <v-icon color="white">mdi-settings</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title class="subtitle-2 font-weight-bold white--text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item @click="goTo('profile')" v-if="$store.state.login == true && $session.get('id')!='admin'">
        <v-list-item-action>
          <v-icon color="white">mdi-account</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title class="subtitle-2 font-weight-bold white--text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <template v-for="(choice, i) in this.$store.state.rightTemp">
        <v-list-item :key="i">
          <v-list-item-action>
            <v-icon color="white">mdi-checkbox-blank</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="subtitle-2 font-weight-bold white--text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>      
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "RightNav",
  data(){
    return{
      drawer: null,
      temp: [],
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
</style>

