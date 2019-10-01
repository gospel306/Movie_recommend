<template >
  <v-navigation-drawer
    v-model="drawer"
    width="4%"
    app
    right
    class="black"
  >
    <v-list>
      <v-list-item @click="goTo('login')">
        <v-list-item-action>
          <v-icon color="white">mdi-account</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title class="subtitle-2 font-weight-bold white--text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <template v-for="(choice, i) in this.$store.state.rightTemp">
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

