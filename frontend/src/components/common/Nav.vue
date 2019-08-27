<template>
  <v-navigation-drawer v-model="drawer" app clipped color="blue lighten-4">
    <v-list dense class="blue lighten-4">
      <template v-for="(choice, i) in choices">
        <v-list-item
          :key="i"
          @click="() => {
              if (choice.path) {
                goTo(choice.path)
              }
            }"
        >
          <v-list-item-action>
            <v-icon>{{ choice.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title class="subtitle-2 font-weight-bold black--text">{{ choice.text }}</v-list-item-title>
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
      choices: [
        {
          icon: "mdi-movie",
          text: "영화 검색",
          path: "search"
        },
        {
          icon: "mdi-account",
          text: "유저 정보",
          path: "userlist"
        }
      ]
    };
  },
  methods: {
      goTo(path){
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

