defmodule Sorter do

  def build_tree(paths) do
    paths
    |> Enum.map(&path_to_tree/1)
    |> Enum.reduce(%{}, &deep_merge/2)
  end

  def path_to_tree(path) do
    pdict = path
    |> String.split("/")
    |> Enum.drop(1)
    |> Enum.reduce([], fn x, paths ->
      parent = Enum.at(paths, 0) || ""
      [parent <> "/" <> x  | paths]
    end)
    |> Enum.reduce(%{}, fn segment, inner_tree ->
      %{segment => inner_tree}
    end)
    %{"/" => pdict}
  end

  def deep_merge(map1, map2) do
    Map.merge(map1, map2, fn _, val1 = %{}, val2 = %{} ->
      deep_merge(val1, val2)
    end)
  end

  def traverse_depth_first(tree) do
    tree
    |> Enum.flat_map(fn {key, subtree} ->
        [key | traverse_depth_first(subtree)]
    end)
  end

  def dft_with_sort([], res, _time_sorted_locs, _indexes), do: res

  def dft_with_sort(stack, res, time_sorted_locs, indexes) do
    {curr, remain} = List.pop_at(stack, -1)

    # case curr == %{} do
    #   true ->
    #     remain |> dft_with_sort(res, time_sorted_locs, indexes)
      
      # false ->

    # just get the key and values of the current map
    {key, values} = List.first(Map.to_list(curr))

    sorter = 
    [Map.get(indexes, key, []) | time_sorted_locs] 
    |> List.flatten()

    new = values
    |> Map.to_list()
    |> Enum.sort_by(&{Enum.find_index(sorter, fn x -> 
      x ==  List.first(Tuple.to_list(&1)) 
    end)})
    |> Enum.map(fn {key, value} -> %{key => value} end)
    |> Enum.reverse()

    res = [key | res]

    [remain | new] 
    |> List.flatten() 
    |> dft_with_sort(res, time_sorted_locs, indexes)
    # end
  end

  def sort(item_list, index_dict) do
    sorted_locs = item_list
    |> Enum.sort_by(&Map.get(&1, "create_time"))
    |> Enum.map(fn x -> Map.get(x, "location") end)

    tree = build_tree(sorted_locs)
    
    dft_with_sort([tree], [], sorted_locs, index_dict) |> Enum.reverse()

  end
end


# The given items
items = [
  %{ "location" => "/folder1", "create_time" => "2019-03-01" },
  %{ "location" => "/folder1/folder1-folder1", "create_time" => "2019-03-02" },
  %{ "location" => "/folder1/folder1-folder1/file1", "create_time" => "2019-03-10" },
  %{ "location" => "/folder1/folder1-folder1/file2", "create_time" => "2019-03-02" },
  %{ "location" => "/folder1/folder1-folder1/file3", "create_time" => "2019-03-04" },
  %{ "location" => "/folder1/folder1-folder1/file4", "create_time" => "2019-03-03" },

  %{ "location" => "/folder2", "create_time" => "2019-01-01" },
  %{ "location" => "/folder2/folder2-folder1", "create_time" => "2019-01-20" },
  %{ "location" => "/folder2/folder2-folder1/file1", "create_time" => "2019-01-22" },
  %{ "location" => "/folder2/folder2-folder1/file2", "create_time" => "2019-01-21" },

  %{ "location" => "/folder2/folder2-folder2", "create_time" => "2019-01-10" },
  %{ "location" => "/folder2/folder2-folder2/file1", "create_time" => "2019-01-11" },
  %{ "location" => "/folder2/folder2-folder2/file2", "create_time" => "2019-01-12" },

  %{ "location" => "/folder3", "create_time" => "2019-02-01" },
  %{ "location" => "/folder3/folder3-folder1", "create_time" => "2019-02-10" },
  %{ "location" => "/folder3/folder3-folder1/file1", "create_time" => "2019-02-12" },
  %{ "location" => "/folder3/folder3-folder1/file2", "create_time" => "2019-02-11" },

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


sorted_locs = items
|> Enum.sort_by(&Map.get(&1, "create_time"))
|> Enum.map(fn x -> Map.get(x, "location") end)

tree = sorted_locs
|> Sorter.build_tree()

Sorter.dft_with_sort([tree], [], sorted_locs, indexes) 
|> Enum.reverse()
|> IO.inspect()

IO.inspect Sorter.sort(items, indexes) == expected



start = Time.utc_now()

range = 1..10000
Enum.map(range, fn _x -> 
  Sorter.sort(items, indexes)
end)

IO.inspect Time.diff(Time.utc_now(), start)

list = ["/2/3/8", "/2/3", "/2/4", "/2/4/6", "/2/3/7", "/2/3/5/6/7/8"]

# map1 = %{"/" => %{"/a" => %{"/a/b" => %{"/a/b/c" => %{"/a/b/c/d" => %{}}}}}}
# map2 = %{"/" => %{"/1" => %{"/1/2" => %{}}}}

# tree = Sorter.build_tree(list)
# |> IO.inspect()

