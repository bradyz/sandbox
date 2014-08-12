class AddExcerptAndLocationToArticles < ActiveRecord::Migration
  def change
    add_column :articles, :excerpt, :string
    add_column :articles, :location, :string
  end
end
