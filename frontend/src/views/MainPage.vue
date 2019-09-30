<template>
  <v-content>
    <LeftNav></LeftNav>
    <RightNav></RightNav>
    <v-container fluid fill-height class="background">
      <router-view></router-view>
    </v-container>
    <h2 class="title is-2">
      Width: {{this.$store.state.window.width}},
      Height: {{this.$store.state.window.height}}
    </h2>
  </v-content>
</template>

<script>
import LeftNav from "@/components/common/LeftNav";
import RightNav from "@/components/common/RightNav";

export default {
  name: "mainpage",
  data: () => ({

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
      this.$store.state.window.width = window.innerWidth;
      this.$store.state.window.height = window.innerHeight;
    }
  },
  mounted() {
  },
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

