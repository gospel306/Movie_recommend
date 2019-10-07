<template >
  <v-navigation-drawer
    v-model="drawer"
    width="3%"
    app
    left
    class="black"    
    >
    <v-layout column justify-center >
      <v-flex id="fir" class="bt" text-sm-right>
        <v-icon color="white" @click="goTo('search')" >mdi-magnify</v-icon>
      </v-flex>
      <v-flex class="bt" text-sm-right>
        <v-icon color="white" @click="goTo('best')">mdi-movie</v-icon>
      </v-flex>
      <v-flex class="bt" text-sm-right>
        <v-icon color="white" @click="goTo('null')">mdi-checkbox-blank</v-icon>
      </v-flex>
      <template v-for="i in this.$store.state.leftNavNum">
        <v-flex class="bt" text-sm-right :key="i">
          <v-icon color="white">mdi-checkbox-blank</v-icon>
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
  margin: 11px 0px;
}
#fir{
  margin-top:20px;
}
</style>

