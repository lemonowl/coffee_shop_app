<template>
  <div v-if="isVisible" class="modal fade show d-block" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Edit Order</h5>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submit">
            <div class="mb-3">
              <input required v-model="formData.number" id="orderNumber" class="form-control" placeholder="Order number">
            </div>
            <div class="mb-3">
              <ul class="list-group list-group-flush">
                <li v-for="(value, index) in formData.items" :key="index" class="list-group-item">
                  <div class="row d-flex justify-content-between align-items-center">
                    <div class="col-md-8">
                      <div class="d-flex justify-content-start align-items-center">
                        <h6 class="me-2">{{ value.name }} <em class="text-muted">$ {{ value.price }}</em></h6>
                      </div>
                      <input v-model="value.comment" placeholder="Comment" class="form-control form-control-sm">
                    </div>
                    <div class="col-md-2">
                      <input v-model.number="value.count" class="form-control form-control-sm">
                    </div>
                    <div class="col-md-2">
                      <button type="button" class="btn btn-sm btn-danger" @click="deleteProduct(index)">Delete</button>
                    </div>
                  </div>
                </li>
              </ul>
              <div class="mt-2">
                <select :required="!formData.items" v-model="selectedProductId" id="productList" class="form-select" @change="addProduct">
                  <option selected disabled value="">Select product to add</option>
                  <option v-for="product in productList" :key="product.id" :value="product.id">
                    {{ product.name }} / {{ product.category }}
                  </option>
                </select>
              </div>
            </div>
            <div class="mb-3">
              <div class="mb-3">
                <label for="orderStatus" class="form-label">Status</label>
                <select :disabled="isNew" v-model="formData.status" class="form-select">
                  <option value="Pending">In progress</option>
                  <option value="Completed">Completed</option>
                  <option value="Cancelled">Cancelled</option>
                </select>
              </div>
            </div>
            <div class="mb-3">
              <textarea v-model="formData.comment" class="form-control" placeholder="Comment"></textarea>
            </div>
            <div class="d-flex justify-content-end align-items-center">
              <button type="submit" class="btn btn-success me-2">Save changes</button>
              <button type="button" class="btn btn-secondary" @click="close">Cancel</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    order: {
      type: Object,
      default: {},
    },
    isVisible: {
      type: Boolean,
    },
    isNew: {
      type: Boolean,
    }
  },
  data() {
    return {
      productList: [],
      selectedProductId: "",
      deletedItems: []
    };
  },
  computed: {
    formData() {
      return {
        ...this.order,
        status: 'Pending',
      };
    },
  },
  methods: {
    getProductList() {
      this.$axios.post('/api/products/get_shortlist')
        .then(response => {
          this.productList = response.data;
        })
        .catch(error => {
          this.$toast.error('Something was wrong...');
        });
    },
    close() {
      this.$emit('closeCard');
    },
    submit() {
      let orderData = this.formData;
      if (this.deletedItems) {
        orderData.items.push(...this.deletedItems);
      }
      this.$emit('updateOrder', orderData);
      this.close();
    },
    addProduct() {
      this.$axios.post('/api/products/get/' + this.selectedProductId)
        .then(response => {
          if ('items' in this.order) {
            this.order.items.push(response.data);
          } else {
            this.order.items = [response.data]
          }
          this.selectedProductId = "";
        })
        .catch(error => {
          this.$toast.error('Something was wrong...');
        });
    },
    deleteProduct(itemIndex) {
      this.deletedItems.push({id: this.order.items[itemIndex].id, deleted: true});
      this.order.items.splice(itemIndex, 1);
    }
  },
  mounted() {
    this.getProductList();
  }
};
</script>