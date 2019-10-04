<template >
  <v-navigation-drawer
    v-model="drawer"
    width="4%"
    app
    left
    class="black"
  >
    <v-list>
      <v-list-item @click="goTo('search')">
        <v-list-item-action>
          <v-icon color="white">mdi-magnify</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title class="subtitle-2 font-weight-bold white--text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item @click="goTo('best')">
        <v-list-item-action>
          <v-icon color="white">mdi-movie</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title class="subtitle-2 font-weight-bold white--text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item @click="goTo('mdi-checkbox-blank')">
        <v-list-item-action>
          <v-icon color="white">mdi-checkbox-blank</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title class="subtitle-2 font-weight-bold white--text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <template v-for="(choice, i) in this.$store.state.leftTemp">
        <v-list-item :key="i">
          <v-list-item-action>
            <v-icon color="white">mdi-checkbox-blank</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="subtitle-2 font-weight-bold white--text"></v-list-item-title>
          </v-list-item-content>
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
</style>

