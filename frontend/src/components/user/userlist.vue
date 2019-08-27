<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <v-flex xs7>
        <h2>하위~</h2>

        <v-layout column>
          <v-flex v-for="card in userListCardsSliced" :key="card.id" pa-2>
            <UserItem
              :id="card.id"
              :age="card.age"
              :gender="card.gender"
              :is_staff="card.is_staff"
              :occupation="card.occupation"
              :username="card.username"
            />
          </v-flex>
          <v-pagination v-if="maxPages > 1" v-model="page" :length="maxPages" />
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
import UserItem from "./useritem";

export default {
  components: {
    UserItem
  },
  data: () => ({
    userLists: [],
    cardsPerPage: 10,
    page: 1
  }),
  computed: {
    userListEmpty: function() {
      return this.userLists.length === 0;
    },
    maxPages: function() {
      return Math.floor((this.userLists.length + this.cardsPerPage - 1) / this.cardsPerPage);
    },
    userListCardsSliced: function() {
      return this.userLists.slice(this.cardsPerPage * (this.page - 1), this.cardsPerPage * this.page);
    }
  },
  mounted () {  
    this.getUserList();
  },
  methods: {
    getUserList() {
      axios
        .get(this.$store.state.server + "/api/-auth/signup-many/")
        .then(res => {
          this.userLists = res.data;
        });
    }
  }
};
</script>