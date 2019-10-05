<template >
  <v-navigation-drawer
    v-model="drawer"
    width="3%"
    app
    left
    class="black"    
  >
    <v-list class="li">
      <v-list-item class="pa-0" @click="goTo('search')">
        <v-list-item-action class="ma-0">
          <v-icon color="white">mdi-magnify</v-icon>
        </v-list-item-action>
      </v-list-item>
      <v-list-item class="pa-0" @click="goTo('best')">
        <v-list-item-action class="ma-0">
          <v-icon color="white">mdi-movie</v-icon>
        </v-list-item-action>
      </v-list-item>
      <v-list-item class="pa-0" @click="goTo('null')">
        <v-list-item-action class="ma-0">
          <v-icon color="white">mdi-checkbox-blank</v-icon>
        </v-list-item-action>
      </v-list-item>
      <template v-for="(choice, i) in this.$store.state.leftTemp">
        <v-list-item class="pa-0" :key="i">
          <v-list-item-action class="ma-0">
            <v-icon color="white">mdi-checkbox-blank</v-icon>
          </v-list-item-action>
        </v-list-item>
      </template>   
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "LeftNav",
  data(){
    return{
      drawer: null,
      leftNavNum: 3,
      temp: [],
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

</style>

