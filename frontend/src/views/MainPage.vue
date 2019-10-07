<template>
  <v-content>
    <v-container fluid fill-height class="back">
      <LeftNav></LeftNav>
      <RightNav></RightNav>
      <v-layout align-center justify-center>        
        <v-flex class="main-board">
          <router-view></router-view>
        </v-flex>
      </v-layout>
    </v-container>
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
      var num = window.innerHeight / 50;
      this.$store.state.leftNavNum = Math.floor(num-3);
      this.$store.state.rightNavNum = Math.floor(num-3);
    }
  },
};
</script>

<style>
.back{
  background-color : black;
  }
.main-board{
  background-color: white;
  border-radius: 15px;
  height: 85%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.ck{
  border-color: aqua;
  border-width:3px;
  border-style: solid;
}
</style>

