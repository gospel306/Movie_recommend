<template >
  <v-navigation-drawer
    v-model="drawer"
    width="4%"
    app
    left
    class="black"
  >
    <v-list>
      <template v-for="(choice, i) in btns">
        <v-list-item
          :key="i"
          @click="() => {
              if (choice.path) {
                goTo(choice.path)
              }
          }"
        >
          <v-list-item-action>
            <v-icon color="white">{{ choice.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="subtitle-2 font-weight-bold white--text">{{ choice.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
      
      <template v-for="(choice, i) in temp">
        <v-list-item
          :key="i"
          @click="() => {
              if (choice.path) {
                goTo(choice.path)
              }
            }"
        >
          <v-list-item-action>
            <v-icon color="white">{{ choice.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="subtitle-2 font-weight-bold white--text">{{ choice.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: "Nav",
  components: {},
  data() {
    return {
      drawer: null,
      btns: [
        {
          icon: "mdi-account",
          path: "profile"
        },
        {
          icon: "mdi-magnify",
          path: "search"
        },
        {
          icon: "mdi-movie",
          path: "best"
        },
        {
          icon: "mdi-checkbox-blank",
          path: "productlist"
        },
      ],
      temp: [
        {
          icon: "mdi-checkbox-blank",
        },  
        {
          icon: "mdi-checkbox-blank",
        },  
        {
          icon: "mdi-checkbox-blank",
        },  
        {
          icon: "mdi-checkbox-blank",
        },  
        {
          icon: "mdi-checkbox-blank",
        },  
        {
          icon: "mdi-checkbox-blank",
        },
        {
          icon: "mdi-checkbox-blank",
        },  
        {
          icon: "mdi-checkbox-blank",
        },  
        {
          icon: "mdi-checkbox-blank",
        },  
        {
          icon: "mdi-checkbox-blank",
        },                
      ], 
    };
  },
  methods: {
    goTo(path) {
      this.$router.push(path);
    }
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

