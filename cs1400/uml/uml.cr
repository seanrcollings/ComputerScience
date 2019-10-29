# Rewriting uml.py in Crystal for practice
class UML
  def initializer(hor_sep : String = "#", ver_sep : String = "#",
                  class_name : String = "", data_members = Array(String),
                  methods = Array(String))
    @hor_sep = hor_sep
    @ver_sep = ver_sep
    @title = "UNIFIED MODELING LANGUAGE"
    @class_name = class_name
    @data_members = data_members
    @methods = methods
    @tableWidth = len(max([@title] + [@class_name] + @data_members + @methods, key = len)) + 3
  end
end
