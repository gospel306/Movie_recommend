<template >
  <v-navigation-drawer
    v-model="drawer"
    width="4%"
    app
    left
    class="black"    
    >
    <v-layout column justify-center text-sm-right>
      <v-flex class="ma-1"/>
      <v-flex  class="ma-2" >
        <v-tooltip right>
          <template v-slot:activator="{ on }">
            <v-btn icon @click="goTo('search')" class="toolbartext" v-on="on">
              <v-icon large color="white"  >mdi-magnify</v-icon>
            </v-btn>
          </template>
          <span>영화검색</span>
        </v-tooltip>
      </v-flex>
      <v-flex  class="ma-2" >
        <v-tooltip right>
          <template v-slot:activator="{ on }">
            <v-btn icon  @click="goTo('best')" class="toolbartext" v-on="on">
             <v-icon large color="white">mdi-movie</v-icon>
            </v-btn>
          </template>
          <span>영화추천</span>
        </v-tooltip>
      </v-flex>
      <template v-for="i in this.$store.state.leftNavNum">
        <v-flex class="ma-2"  :key="i">
          <v-tooltip right>
            <template v-slot:activator="{ off }">
              <v-btn icon class="toolbartext" v-on="on">
                <v-icon large color="white">mdi-checkbox-blank</v-icon>
              </v-btn>
            </template>            
          </v-tooltip>
        </v-flex>
      </template>   
    </v-layout>
  </v-navigation-drawer>
</template>

<script>

export default {
  name: "LeftNav",
  data(){
    return{
      drawer: null,
    }
  },
  methods: {
    goTo(path) {
      this.$router.push(path);
    },
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
.li{
  float: right;
}
.bt{
  margin: 0px 0px;
}
#fir{
  margin-top:10px;
}
</style>

