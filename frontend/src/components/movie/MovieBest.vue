<template>
  <v-container text-center>
    <h1>추천 영화</h1>
    <v-layout row fill-height>
      <v-sheet class="mx-auto" elevation="8" max-width="90%">
        <v-slide-group v-model="model" class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="n in 15" :key="n" v-slot:default="{ active, toggle }">
            <v-card
              :color="active ? undefined : 'grey lighten-1'"
              class="ma-4"
              height="500"
              width="250"
              @click="toggle"
            >
              <v-row class="fill-height" align="center" justify="center">
                <v-scale-transition>
                  <v-icon v-if="active" color="white" size="48" v-text="'mdi-close-circle-outline'"></v-icon>
                </v-scale-transition>
              </v-row>
            </v-card>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      model: null
    };
  }
};
</script>