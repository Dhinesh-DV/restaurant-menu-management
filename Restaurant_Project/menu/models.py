from django.db import models


class Chef(models.Model):
    """Represents a chef in the restaurant."""
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    """Represents a menu category (e.g., Starter, Main, Dessert)."""
    name = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Represents a menu item."""
    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    chef = models.ForeignKey(
        Chef,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name


class DiningTable(models.Model):
    """Represents a dining table."""
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField(default=2)
    
    def __str__(self):
        return f"Table {self.table_number}"
