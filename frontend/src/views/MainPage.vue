<template>
  <v-content>
    <v-container fluid fill-height class="back">
     <v-layout align-center justify-center>
        <v-flex class="main-board">
          <router-view></router-view>
        </v-flex>
      </v-layout>
    </v-container>
    <LeftNav class="nav"></LeftNav>
    <RightNav class="nav"></RightNav>
  </v-content>
</template>

<script>
/*
    <LeftNav class="nav"></LeftNav>
    <RightNav class="nav"></RightNav>
*/
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
.back{
  background-color : black;
  }
  /*
    border-width: 1px;
  border-color: blue;
  border-style : solid;

    border-width: 5px;
  border-color: aqua;
  border-style : solid;
  margin : 10px;

   */
.main-board{
  background-color: white;
  border-radius: 30px;
  height: 85%;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>

