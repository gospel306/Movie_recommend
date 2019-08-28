<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :elevation="hover ? 8 : 2">
      <v-layout align-center py-4 pl-4>
        <v-flex text-center>
          <v-container grid-list-lg pa-0>
            <v-layout column>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="headline">
                    {{ username }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-card-text>
                <v-layout justify-center>
                  <div class="grey--text ml-4">{{ gender }}, {{ age }}</div>
                </v-layout>
              </v-card-text>
            </v-layout>
          </v-container>
        </v-flex>
      </v-layout>

      <UserDetail
        :id="id"
        :age="age"
        :gender="gender"
        :is_staff="is_staff"
        :occupation="occupation"
        :username="username"
      />

    </v-card>
  </v-hover>
</template>

<script>
import UserDetail from "@/components/user/UserDetail"

export default {
  components: {
    UserDetail,
  },
  props: {
    id: {
      type: Number,
      default: 0
    },
    username: {
      type: String,
      default: ""
    },
    occupation: {
      type: String,
      default: ""
    },
    gender: {
      type: String,
      default: ""
    },
    is_staff: {
      type: Boolean,
      default: false
    },                                                                                                                                                                   
    age: {
      type: Number,
      default: 0
    }
  },
  computed: {
    // genreSplit() {
    //   var str = this.genres
    //   return str.replace(/\|/g," / ")
    // }
  }
};
</script>