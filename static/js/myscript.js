function updateFilterPlaceholders() {
  var categoryFilter = document.getElementById('category-filter');
  var kitchenFilter = document.getElementById('kitchen-filter');
  var testedFilter = document.getElementById('tested-filter');
  
  var categoryPlaceholder = categoryFilter.options[categoryFilter.selectedIndex].text;
  var kitchenPlaceholder = kitchenFilter.options[kitchenFilter.selectedIndex].text;
  var testedPlaceholder = testedFilter.options[testedFilter.selectedIndex].text;
  
  if (categoryPlaceholder === 'All') {
    categoryPlaceholder = 'Category';
  }
  
  if (kitchenPlaceholder === 'All') {
    kitchenPlaceholder = 'Kitchen';
  }
  
  if (testedPlaceholder === 'All') {
    testedPlaceholder = 'Tested';
  }
  
  categoryFilter.setAttribute('placeholder', categoryPlaceholder);
  kitchenFilter.setAttribute('placeholder', kitchenPlaceholder);
  testedFilter.setAttribute('placeholder', testedPlaceholder);
  
  // Store the selected filter values in local storage
  localStorage.setItem('selectedCategory', categoryFilter.value);
  localStorage.setItem('selectedKitchen', kitchenFilter.value);
  localStorage.setItem('selectedTested', testedFilter.value);
  
}

function updateFilterPlaceholdersFromStorage() {
  var categoryFilter = document.getElementById('category-filter');
  var kitchenFilter = document.getElementById('kitchen-filter');
  var testedFilter = document.getElementById('tested-filter');
  
  var selectedCategory = localStorage.getItem('selectedCategory');
  var selectedKitchen = localStorage.getItem('selectedKitchen');
  var selectedTested = localStorage.getItem('selectedTested');
  
  if (selectedCategory) {
    categoryFilter.value = selectedCategory;
  }
  
  if (selectedKitchen) {
    kitchenFilter.value = selectedKitchen;
  }
  
  if (selectedTested) {
    testedFilter.value = selectedTested;
  }
  
  updateFilterPlaceholders();
  
}

function resetFilters() {
  // Reset filter values
  document.getElementById("category-filter").value = "";
  document.getElementById("kitchen-filter").value = "";
  document.getElementById("tested-filter").value = "";
  document.getElementById("search-filter").value = "";

  
  // Reset filter placeholders to default values
  updateFilterPlaceholders();
  
  // Submit form to reset view
  document.querySelector("form").submit();
}

// Add event listener to reset button
document.addEventListener('DOMContentLoaded', function() {
  const removeFiltersButton = document.querySelector('.remove-filters-button');

  removeFiltersButton.addEventListener('click', function() {
    // Your event handling code here
  });
});


// Checkbox on-click event
document.addEventListener('DOMContentLoaded', function() {
  const checkboxes = document.querySelectorAll('.tested-checkbox');

  checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function(event) {
      const targetCheckbox = event.target;
      const recipeId = targetCheckbox.dataset.id;
      const isChecked = targetCheckbox.checked;

      // Get the CSRF token from the cookie
      const csrftoken = getCookie('csrftoken');

      // Send AJAX request to update_recipe view
      const xhr = new XMLHttpRequest();
      xhr.open('POST', '/update_recipe/');
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      xhr.setRequestHeader('X-CSRFToken', csrftoken); // Include the CSRF token in the request header
      xhr.onload = function() {
        if (xhr.status === 200) {
          console.log('Recipe updated successfully');
        } else {
          console.error('Error updating recipe');
        }
      };
      xhr.onerror = function() {
        console.error('Error updating recipe');
      };
      xhr.send(`recipe_id=${recipeId}&is_checked=${isChecked}`);
    });
  });
});


// Helper function to get the CSRF token from the cookie
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

// delete button
document.addEventListener('DOMContentLoaded', function() {
  const checkboxes = document.querySelectorAll('.tested-checkbox');

  checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function(event) {
      const targetCheckbox = event.target;
      const recipeId = targetCheckbox.dataset.id;
      const isChecked = targetCheckbox.checked;

      // Get the CSRF token from the cookie
      const csrftoken = getCookie('csrftoken');

      // Send AJAX request to update_recipe view
      const xhr = new XMLHttpRequest();
      xhr.open('POST', '/update_recipe/');
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      xhr.setRequestHeader('X-CSRFToken', csrftoken); // Include the CSRF token in the request header
      xhr.onload = function() {
        if (xhr.status === 200) {
          console.log('Recipe updated successfully');
        } else {
          console.error('Error updating recipe');
        }
      };
      xhr.onerror = function() {
        console.error('Error updating recipe');
      };
      xhr.send(`recipe_id=${recipeId}&is_checked=${isChecked}`);
    });
  });

  const deleteIcons = document.querySelectorAll('.delete-icon');

  deleteIcons.forEach(function(icon) {
    icon.addEventListener('click', function(event) {
      event.preventDefault();

      const recipeId = this.dataset.id;

      const confirmDelete = confirm('Are you sure you want to delete this recipe?');
      if (confirmDelete) {
        // Get the CSRF token from the cookie
        const csrftoken = getCookie('csrftoken');

        // Send AJAX request to delete_recipe view
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/delete_recipe/');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.setRequestHeader('X-CSRFToken', csrftoken); // Include the CSRF token in the request header
        xhr.onload = function() {
          if (xhr.status === 200) {
            console.log('Recipe deleted successfully');
            // Optionally, you can remove the deleted recipe row from the table
            const row = icon.closest('tr');
            row.remove();
          } else {
            console.error('Error deleting recipe');
          }
        };
        xhr.onerror = function() {
          console.error('Error deleting recipe');
        };
        xhr.send(`recipe_id=${recipeId}`);
      }
    });
  });
});

//check if recipe exists
window.addEventListener('DOMContentLoaded', function() {
  if ("{{ existing_recipe }}" === "True") {
    alert("{{ message }}");
  }
});