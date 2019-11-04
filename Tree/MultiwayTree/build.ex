defmodule Tree do

  def build_tree(list) do
    list
    |> Enum.reverse()
    |> Enum.reduce(%{}, fn foo, map ->
      foo = %{foo | children: Map.get(map, foo.location, [])}
      Map.update(map, foo.parent, [foo], fn foos ->
        [foo | foos]
      end)
    end)
    |> Map.get(nil)
    |> hd
  end
end

items = [
  %{ location: "/", parent: nil, children: [] },
  %{ location: "/folder1", parent: "/", children: [] },
  %{ location: "/folder1/folder1-folder1", parent: "/folder1", children: [] },
  %{ location: "/folder2", parent: "/", children: [] },
  %{ location: "/folder2/folder2-folder1", parent: "/folder2", children: [] }
]


Tree.build_tree(items)
|> IO.inspect()
