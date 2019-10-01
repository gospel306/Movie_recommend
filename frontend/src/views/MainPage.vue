<template>
  <v-content>
    <v-container fluid fill-height class="background">
      <router-view></router-view>
    </v-container>
    <LeftNav></LeftNav>
    <RightNav></RightNav>
  </v-content>
</template>

<script>
import LeftNav from "@/components/common/LeftNav";
import RightNav from "@/components/common/RightNav";

export default {
  name: "mainpage",
  data: () => ({
    window:{
      width: 0,
      height: 0,
    }
  }),
  components: {
    LeftNav,
    RightNav
  },
  created() {
    window.addEventListener('resize', this.handleResize)
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    handleResize() {
      this.window.width = window.innerWidth;
      this.window.height = window.innerHeight;
      var leftNum = this.window.height / 49 - this.$store.state.leftNum;
      var rightNum = this.window.height / 49 - this.$store.state.rightNum;
      this.$store.state.leftTemp.length = 0;
      this.$store.state.rightTemp.length = 0;

      for(var i = 1; i <= leftNum; i++){
        this.$store.state.leftTemp.push(i);
      };
      for(var i = 1; i <= rightNum; i++){
        this.$store.state.rightTemp.push(i);
      };
    }
  },
};
</script>

<style>
/* .background{
  background: url("http://image.downloadwap.co.uk/wallpapers/p2ls/new/38/wallp_hVnXsXu8uw.jpg");
} */
/*
 .background{
  background: black
} */
 .background{
  background: url("../images/back1.png");
  background-repeat: no-repeat;
  background-size: 104% 100%;
  background-position: center;
} 

</style>

