<template>
  <v-toolbar flat color="info" class="subtoolbar">
    <v-spacer />
    <v-toolbar-items>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-flex align-self-center>
            <v-btn icon @click="signup" v-if="$store.state.login === false " v-on="on">
              <v-icon class="toolbartext" color="black">mdi-account-plus</v-icon>
            </v-btn>
          </v-flex>
        </template>
        <span>회원가입</span>
      </v-tooltip>

      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-flex align-self-center>
            <v-btn icon to="/admin" v-if="$store.state.login === true && $session.get('username') == 'admin'" v-on="on">
              <v-icon class="adminicon">mdi-settings</v-icon>
            </v-btn>
          </v-flex>
        </template>
        <span>관리자 페이지</span>
      </v-tooltip>

      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-flex align-self-center>
            <v-btn icon @click="loginForm" v-if="$store.state.login === false " v-on="on">
              <v-icon class="toolbartext" color="black">mdi-open-in-app</v-icon>
            </v-btn>
          </v-flex>
        </template>
        <span>로그인</span>
      </v-tooltip>

      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-flex align-self-center>
            <v-btn icon @click="profilePage" v-if="$store.state.login === true && $session.get('username') != 'admin'" v-on="on">
              <v-icon class="toolbartext" color="black">mdi-account</v-icon>
            </v-btn>
          </v-flex>
        </template>
        <span>회원정보</span>
      </v-tooltip>

      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-flex align-self-center>
            <v-btn icon @click="logoutForm" v-if="$store.state.login === true " v-on="on">
              <v-icon class="toolbartext" color="black">mdi-exit-to-app</v-icon>
            </v-btn>
          </v-flex>
        </template>
        <span>로그아웃</span>
      </v-tooltip>
    </v-toolbar-items>

    <v-dialog v-model="logoutDialog" max-width="290">
      <v-card>
        <v-card-title class="headline">로그아웃 하시겠습니까?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="grey darken-2"
            class="white--text"
            flat="flat"
            @click="logoutDialog = false"
          >아니오</v-btn>
          <v-btn color="grey darken-2" class="white--text" flat="flat" @click="logout()">예</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-toolbar>
</template>

<script>
export default {
  data() {
    return {
      drawer: null,
      logoutDialog: false
    };
  },
  methods: {
    logoutForm() {
      this.logoutDialog = true;
    },
    logout() {
      this.logoutDialog = false;
      this.$store.state.login = false;
      this.$session.clear();
      this.$router.push("/");
    },
    loginForm(){
      this.$router.push('/login');
    },
    signup(){
      this.$router.push('/signup');
    },
    profilePage(){
      this.$router.push('/profile');
    }
  },
};
</script>
<style scoped>
.subtoolbar {
  z-index: 100;
}
.toolbartext {
  text-shadow: 1px 1px 5px black;
  color: rgb(47, 97, 105);
}
.adminicon {
  color: rgb(5, 5, 5) !important;
  text-shadow: 1px 1px 3px rgb(129, 129, 129);
}
</style>
