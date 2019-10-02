<template>
  <v-container grid-list-md >
    <v-layout justify-center wrap>  
      <v-flex xs7>
        <h3>평점 목록</h3>
        <MyRatingItem :MyRatingItems="ratingList"/>
        <v-progress-circular :size="50" color="primary" indeterminate v-if="loading"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
import MyRatingItem from "@/components/profile/MyRatingItem";

export default {
  components: {
    MyRatingItem
  },
  data: () => ({
    ratingList: [],
    loading: false,
  }),
  mounted () {  
    this.getRatingList();
  },
  methods: {
    getRatingList(){
        this.loading = true;
        axios.get(this.$store.state.server + "/api/ratings/?username="+this.$session.get('id')).then(res => {
          this.ratingList = res.data;
          this.loading = false;
        });
    }
  }
};
</script>