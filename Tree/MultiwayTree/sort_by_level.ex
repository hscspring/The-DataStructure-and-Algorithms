defmodule Sorter do

  def build_item_level(item_list) do
    item_list 
    |> Enum.sort_by(&Map.get(&1, "create_time"))
    |> Enum.map(fn x -> Map.get(x, "location") end)
    |> build_location_level()
  end

  def build_index_level(index_dict) do
    index_dict
    |> Enum.reduce([], fn {_, children}, index_list ->
      [children | index_list]
    end)
    |> Enum.reverse()
    |> List.flatten()
    |> build_location_level()
  end

  defp build_location_level(location_list) do
    location_list
    |> Enum.reduce(%{}, fn loc, loc_level ->
      level = Enum.count(String.split(loc, "/"))
      items = Map.get(loc_level, level, []) ++ [loc]
      Map.put(loc_level, level, items)
    end)
  end

  def combine_item_index_level(item_level, index_level) do
    Enum.reduce(item_level, %{}, fn {level, items}, combined_level ->
    index = Map.get(index_level, level, [])
    not_in_index = Enum.filter(items, fn x ->
      Enum.member?(index, x) == false
    end)
    combined = index ++ not_in_index
    Map.put(combined_level, level, combined)
    end)
  end

  def sort_level_items(combined_level) do
    combined_level
    |> Enum.reduce(%{}, fn {level, items}, sorted_items ->
    standard = Map.get(sorted_items, level-1, [])
    sorted = Enum.sort_by(items, &Enum.find_index(standard, fn x ->
      x == get_parent_location(&1)
    end))
    Map.put(sorted_items, level , sorted)
    end)
  end

  def get_parent_location(path) do
    path
    |> String.split("/")
    |> Enum.slice(0..-2)
    |> get_parent_helper()
  end

  defp get_parent_helper([]), do: ""
  defp get_parent_helper([""]), do: "/"
  defp get_parent_helper(loc_list), do: Enum.join(loc_list, "/")

  def combine_sorted_items(sorted_items) do
    locs_dict = %{"/" => "00000"}
    sorted_items
    |> Enum.reduce([], fn {_, items}, level_list ->
      [items | level_list]
    end)
    |> Enum.reverse()
    |> add_tag_to_location(locs_dict)
    |> Enum.sort_by(fn {_, tag} -> tag end)
    |> Enum.map(fn {loc, _} -> loc end)
  end

  defp add_tag_to_location([], locs_dict), do: locs_dict
  defp add_tag_to_location([group | groups], locs_dict) do
    loc_dict = group
    |> Enum.with_index(1)
    |> Enum.reduce(%{}, fn {item, id}, loc_dict ->
      parent_tag = Map.get(locs_dict, get_parent_location(item))
      tag = String.pad_leading(Integer.to_string(id), 5, "0")
      Map.put(loc_dict, item, parent_tag <> "-" <> tag)
    end)
    locs_dict = Map.merge(locs_dict, loc_dict)
    add_tag_to_location(groups, locs_dict)
  end

  def sort(item_list, index_dict) do
    index_level = build_index_level(index_dict)
    item_list
    |> build_item_level()
    |> combine_item_index_level(index_level)
    |> sort_level_items()
    |> combine_sorted_items() 
  end
end


# The given items
items = [
  %{ "location" => "/folder1", "create_time" => "2019-03-01" },
  %{ "location" => "/folder1/folder1-folder1", "create_time" => "2019-03-02" },
  %{ "location" => "/folder1/folder1-folder1/file1", "create_time" => "2019-03-10" },
  %{ "location" => "/folder1/folder1-folder1/file2", "create_time" => "2019-03-01" },
  %{ "location" => "/folder1/folder1-folder1/file3", "create_time" => "2019-03-03" },
  %{ "location" => "/folder1/folder1-folder1/file4", "create_time" => "2019-03-02" },

  %{ "location" => "/folder2", "create_time" => "2019-01-01" },
  %{ "location" => "/folder2/folder2-folder1", "create_time" => "2019-01-20" },
  %{ "location" => "/folder2/folder2-folder1/file1", "create_time" => "2019-01-22" },
  %{ "location" => "/folder2/folder2-folder1/file2", "create_time" => "2019-01-21" },

  %{ "location" => "/folder2/folder2-folder2", "create_time" => "2019-01-10" },
  %{ "location" => "/folder2/folder2-folder2/file1", "create_time" => "2019-01-11" },
  %{ "location" => "/folder2/folder2-folder2/file2", "create_time" => "2019-01-12" },

  %{ "location" => "/folder3", "create_time" => "2019-02-01" },
  %{ "location" => "/folder3/folder3-folder1", "create_time" => "2019-02-10" },
  %{ "location" => "/folder3/folder3-folder1/file1", "create_time" => "2019-02-02" },
  %{ "location" => "/folder3/folder3-folder1/file2", "create_time" => "2019-02-01" },

  %{ "location" => "/folder3/folder3-folder2", "create_time" => "2019-02-01" },
  %{ "location" => "/folder3/folder3-folder2/file1", "create_time" => "2019-02-03" },
  %{ "location" => "/folder3/folder3-folder2/file2", "create_time" => "2019-02-04" },

  %{ "location" => "/folder3/folder3-folder3", "create_time" => "2019-02-03" },
  %{ "location" => "/folder3/folder3-folder3/file1", "create_time" => "2019-02-05" },
  %{ "location" => "/folder3/folder3-folder3/file2", "create_time" => "2019-02-04" },

  %{ "location" => "/folder3/folder3-folder4", "create_time" => "2019-02-02" }
]

# The given index dict
indexes = %{
  "/folder1/folder1-folder1" => [
    "/folder1/folder1-folder1/file1",
    "/folder1/folder1-folder1/file2"
  ],
  "/folder2/folder2-folder1" => [
    "/folder2/folder2-folder1/file1",
    "/folder2/folder2-folder1/file2",
  ],
  "/folder2/folder2-folder2" => [
    "/folder2/folder2-folder2/file1",
    "/folder2/folder2-folder2/file2"
  ],
  "/folder3" => [
    "/folder3/folder3-folder1",
    "/folder3/folder3-folder2"
  ],
}

# need result
expected = [
  "/",
  "/folder2",
  "/folder2/folder2-folder2",
  "/folder2/folder2-folder2/file1",
  "/folder2/folder2-folder2/file2",
  "/folder2/folder2-folder1",
  "/folder2/folder2-folder1/file1",
  "/folder2/folder2-folder1/file2",
  "/folder3",
  "/folder3/folder3-folder1",
  "/folder3/folder3-folder1/file2",
  "/folder3/folder3-folder1/file1",
  "/folder3/folder3-folder2",
  "/folder3/folder3-folder2/file1",
  "/folder3/folder3-folder2/file2",
  "/folder3/folder3-folder4",
  "/folder3/folder3-folder3",
  "/folder3/folder3-folder3/file2",
  "/folder3/folder3-folder3/file1",
  "/folder1",
  "/folder1/folder1-folder1",
  "/folder1/folder1-folder1/file1",
  "/folder1/folder1-folder1/file2",
  "/folder1/folder1-folder1/file4",
  "/folder1/folder1-folder1/file3"
]


item_level = Sorter.build_item_level(items)
index_level = Sorter.build_index_level(indexes)

combined_level = Sorter.combine_item_index_level(item_level, index_level)
sorted_level_items = Sorter.sort_level_items(combined_level)

Sorter.combine_sorted_items(sorted_level_items)
|>IO.inspect()

IO.inspect(Sorter.sort(items, indexes) == expected)


