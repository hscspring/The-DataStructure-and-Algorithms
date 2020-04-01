defmodule Sorter do

  def build_tree(list, index_dict) do
    tree = list
    |> Enum.reduce(%{}, fn foo, map ->
      foo = %{foo | children: Map.get(map, foo.location, [])}

      Map.update(map, foo.parent, [foo], fn foos ->
        children = [foo | foos]

        case Map.get(index_dict, foo.parent) do
          nil ->
            children

          index_list ->
            children
            |> Enum.sort_by(&(Enum.find_index(index_list, fn item ->
              item == &1.location
            end)))
        end
      end)
    end)
    |> Map.get(nil)
  end

  def dft([], res), do: res
  def dft(stack, res) do
    {curr, remain} = List.pop_at(stack, -1)
    res = [curr.location | res]
    [remain | Enum.reverse(curr.children)] 
    |> List.flatten()
    |> dft(res)
  end

  def sort(item_list, index_dict) do
    item_list
    |> Enum.sort_by(& &1.create_time)
    |> add_parent()
    |> build_tree(index_dict)
    |> dft([])
    |> Enum.reverse()
  end

  def add_parent(item_list) do
    init = %{location: "/", parent: nil, children: []}
    item_list
    |> Enum.reduce([init], fn item, new_list ->
      parent = get_parent(item.location)
      new_item = %{location: item.location, parent: parent, children: []}
      [new_item | new_list]
    end)
  end

  def get_parent(path) do
    path
    |> String.split("/")
    |> Enum.slice(0..-2)
    |> get_parent_helper()
  end

  defp get_parent_helper([""]), do: "/"
  defp get_parent_helper(loc_list), do: Enum.join(loc_list, "/")
end


# The given items
items = [
  %{ location: "/folder1", create_time: "2019-03-01" },
  %{ location: "/folder1/folder1-folder1", create_time: "2019-03-02" },
  %{ location: "/folder1/folder1-folder1/file1", create_time: "2019-03-10" },
  %{ location: "/folder1/folder1-folder1/file2", create_time: "2019-03-02" },
  %{ location: "/folder1/folder1-folder1/file3", create_time: "2019-03-04" },
  %{ location: "/folder1/folder1-folder1/file4", create_time: "2019-03-03" },

  %{ location: "/folder2", create_time: "2019-01-01" },
  %{ location: "/folder2/folder2-folder1", create_time: "2019-01-20" },
  %{ location: "/folder2/folder2-folder1/file1", create_time: "2019-01-22" },
  %{ location: "/folder2/folder2-folder1/file2", create_time: "2019-01-21" },

  %{ location: "/folder2/folder2-folder2", create_time: "2019-01-10" },
  %{ location: "/folder2/folder2-folder2/file1", create_time: "2019-01-11" },
  %{ location: "/folder2/folder2-folder2/file2", create_time: "2019-01-12" },

  %{ location: "/folder3", create_time: "2019-02-01" },
  %{ location: "/folder3/folder3-folder1", create_time: "2019-02-10" },
  %{ location: "/folder3/folder3-folder1/file1", create_time: "2019-02-12" },
  %{ location: "/folder3/folder3-folder1/file2", create_time: "2019-02-11" },

  %{ location: "/folder3/folder3-folder2", create_time: "2019-02-01" },
  %{ location: "/folder3/folder3-folder2/file1", create_time: "2019-02-03" },
  %{ location: "/folder3/folder3-folder2/file2", create_time: "2019-02-04" },

  %{ location: "/folder3/folder3-folder3", create_time: "2019-02-03" },
  %{ location: "/folder3/folder3-folder3/file1", create_time: "2019-02-05" },
  %{ location: "/folder3/folder3-folder3/file2", create_time: "2019-02-04" },

  %{ location: "/folder3/folder3-folder4", create_time: "2019-02-02" }
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


Sorter.sort(items, indexes)
|> IO.inspect()

IO.inspect Sorter.sort(items, indexes) == expected



start = Time.utc_now()

range = 1..10000
Enum.map(range, fn _x -> 
  Sorter.sort(items, indexes)
end)

IO.inspect Time.diff(Time.utc_now(), start)


items
|> Enum.sort_by(& &1.create_time)
|> Sorter.add_parent()
|> IO.inspect()
|> Sorter.build_tree(indexes)
|> IO.inspect()
