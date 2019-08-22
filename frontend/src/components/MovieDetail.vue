<template>
  <div>
    <v-row justify="center">
      <v-btn
        color="primary"
        class="ma-2"
        dark
        @click="dialog = true">
        상세보기
      </v-btn>

      <v-dialog
        v-model="dialog"
        hide-overlay
        transition="dialog-bottom-transition"
        scrollable
        max-width="500px">
        <v-card tile>
          <v-toolbar
            flat
            dark
            color="primary"
          >
            <v-toolbar-title>영화 상세정보</v-toolbar-title>
            <div class="flex-grow-1"></div>
            <v-toolbar-items>
            <v-btn
              icon
              dark
              @click="dialog = false"
            >
              <v-icon>close</v-icon>
            </v-btn>
            </v-toolbar-items>
          </v-toolbar>
          <v-card-text>

            <v-list three-line subheader>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>영화 제목</v-list-item-title>
                  <v-list-item-subtitle>{{ title }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>영화 장르</v-list-item-title>
                  <v-list-item-subtitle>{{ genreSplit }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>영화 평점</v-list-item-title>
                  <v-list-item-subtitle>{{ ratingRounds }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>

            <v-divider></v-divider>
            <v-list three-line subheader>
                <v-subheader>해당 영화를 본 사람들</v-subheader>
                <v-list disabled dense sm5 md5 lg5>
                    <v-list-item
                        v-for="(item, i) in items"
                        :key="i"
                        @click="() => {}"
                    >
                        <v-list-item-content>
                            <v-list-item-title>{{ item.username }}</v-list-item-title>
                            <v-list-item-subtitle>{{ item.gender }}, {{ item.age }}, {{ item.occupation }}</v-list-item-subtitle>
                            <v-list-item-subtitle>{{ item.rating }}</v-list-item-subtitle>
                        </v-list-item-content>    
                    </v-list-item>
                </v-list>
            </v-list>
          </v-card-text>

          <div style="flex: 1 1 auto;"></div>
        </v-card>
      </v-dialog>

    </v-row>
  </div>
</template>

<script>
  export default {
    props: {
        title: {
        type: String,
        default: ""
        },
        genres: {
        type: String,
        default: ""
        },
        rating: {
        type: Number,
        default: 0.0
        }
    },
    data () {
      return {
        dialog: false,
        items: [
            {
                username: '노현우',
                age: '27',
                occupation: '백수',
                gender: 'M',
                rating: '2.7'
            },
            {
                username: '김동욱',
                age: '27',
                occupation: '백수',
                gender: 'm',
                rating: '3.1'
            },
            {
                username: '김경태',
                age: '26',
                occupation: '백수',
                gender: 'M',
                rating: '4.0'
            },
            {
                username: '조수장',
                age: '27',
                occupation: '백수',
                gender: 'M',
                rating: '3.9'
            }
        ],
      }
    },
  computed: {
    genreSplit() {
        var str = this.genres
        return str.replace(/\|/g," / ")
    },
    ratingRounds() {
        var num = this.rating
        return num.toFixed(2)
    }
  },
  }
</script>