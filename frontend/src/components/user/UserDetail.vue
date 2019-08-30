<template>
  <div>
    <v-row justify="center">
      <v-btn color="primary" class="ma-2" dark @click="dialog = true; searchMovie(id)">상세보기</v-btn>

      <v-dialog
        v-model="dialog"
        hide-overlay
        transition="dialog-bottom-transition"
        scrollable
        max-width="500px"
      >
        <v-card tile>
          <v-toolbar flat dark color="primary">
            <v-toolbar-title>유저 상세정보</v-toolbar-title>
            <div class="flex-grow-1" />
            <v-toolbar-items>
              <v-btn icon dark @click="dialog = false">
                <v-icon>close</v-icon>
              </v-btn>
            </v-toolbar-items>
          </v-toolbar>
          <v-card-text>
            <v-list three-line subheader>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>유저 이름</v-list-item-title>
                  <v-list-item-subtitle>{{ username }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>성별, 나이</v-list-item-title>
                  <v-list-item-subtitle>{{ gender }}, {{ age }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>직업</v-list-item-title>
                  <v-list-item-subtitle>{{ occupation }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>

            <v-divider />
            <v-list three-line subheader>
              <v-subheader>해당 유저가 본 영화</v-subheader>
              <v-list disabled dense sm5 md5 lg5>
                <v-list-item v-if="!items.length">
                  <v-list-item-title>본 영화가 없습니다</v-list-item-title>
                </v-list-item>
                <v-list-item v-for="(item, i) in items" :key="i" @click="() => {}">
                  <v-list-item-content>
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                    <v-list-item-subtitle>{{ item.genres }}</v-list-item-subtitle>
                    <v-list-item-subtitle>
                        <v-rating
                            :value="item.rating"
                            color="indigo"
                            background-color="indigo"
                            half-increments
                            dense
                            small
                            readonly
                            />
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-list>
          </v-card-text>
          <div style="flex: 1 1 auto;" />
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";

export default {
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
  data() {
    return {
      dialog: false,
      items: []
    };
  },
  computed: {
    genreSplit(input) {
        var str = input;
        return str.replace(/\|/g, " / ");
    }
  },
  methods: {
    searchMovie: function(id) {
      axios
      .get(this.$store.state.server + "/api/auth/signup-many/?userid=" + id)
      .then(res => {
        this.items = res.data;
      });
    }
  }
};
</script>