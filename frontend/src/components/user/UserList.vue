<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <v-flex xs7>
        <h2>유저 목록</h2>
        <UserItem :UserItems="userLists"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
import UserItem from "@/components/user/UserItem";

export default {
  components: {
    UserItem
  },
  data: () => ({
    userLists: [],
  }),
  mounted () {  
    this.getUserList();
  },
  methods: {
    getUserList() {
      axios
        .get(this.$store.state.server + "/api/-auth/signup-many/")
        .then(res => { // 이부분에 프로미스를 써주자
          this.userLists = res.data;
        });
    }
  }
};
</script>