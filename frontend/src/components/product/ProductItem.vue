<template>
  <v-card class="mx-auto" max-width="100%" outlined>
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4">{{headline}}</div>
        <v-list-item-title class="headline mb-1">{{title}}</v-list-item-title>
        <v-list-item-subtitle>{{subtitle}}</v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar tile size="100" color="grey"></v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-btn text>구독</v-btn>
      <v-btn text>좋아요</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    headline: {
      type: String,
      default: ""
    },
    title: {
      type: String,
      default: ""
    },
    subtitle: {
      type: String,
      default: ""
    },
  },
  computed: {
    
  },
};
</script>