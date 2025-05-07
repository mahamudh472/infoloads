function validateSearch(parent) {
    const searchInput = parent.querySelector('.searchInput').value.trim();
    if (!searchInput) {
      return false;
    }
    return true;
  }