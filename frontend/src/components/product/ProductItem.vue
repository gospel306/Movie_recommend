<template>
  <v-card class="mx-auto" max-width="100%" outlined>
    <v-list-item three-line>
      <v-list-item-content>
        <v-list-item-title class="headline mb-1">{{title}}</v-list-item-title>
        <div class="overline mb-4">구독자 수: {{subscriber}} 명</div>
        <v-list-item-subtitle>{{subtitle}}</v-list-item-subtitle>
      </v-list-item-content>

      <v-btn color="red darken-2" class="white--text">구독</v-btn>
    </v-list-item>
  </v-card>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: ""
    },
    subscriber: {
      type: String,
      default: ""
    },
    subtitle: {
      type: String,
      default: ""
    }
  },
  computed: {}
};
</script>