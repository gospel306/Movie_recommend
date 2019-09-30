<template>
  <v-content>
    <Header></Header>
    <LeftNav></LeftNav>
    <RightNav></RightNav>
    <v-container fluid fill-height class="background">
      <router-view></router-view>
    </v-container>
  </v-content>
</template>

<script>
import LeftNav from "@/components/common/LeftNav";
import RightNav from "@/components/common/RightNav";

export default {
  name: "mainpage",
  data() {
    return {};
  },
  components: {
    LeftNav,
    RightNav
  },
  mounted() {},
  methods: {}
};
</script>

<style>
/* .background{
  background: url("http://image.downloadwap.co.uk/wallpapers/p2ls/new/38/wallp_hVnXsXu8uw.jpg");
} */

 .background{
  background: black
} 
</style>

