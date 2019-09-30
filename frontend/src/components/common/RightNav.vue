<template>
  <v-navigation-drawer
    v-model="drawer_right"
    width="4%"
    app
    right
    class="black"
  >
    <v-list >
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
      drawer_right: null,
      btns: [
        {
          icon: "mdi-login",
          path: "login",
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
</style>

