# Getter and setters in Python

|  Feature      |  @property                        | 	@radius.getter                                                |
| ------------- | --------------------------------- | --------------------------------------------------------------- | 
|Primary Purpose| Defines a getter for an attribute | Explicitly defines the getter (useful with setters & deleters)  |
|Required?      | No, but makes a method behave     | No, unless you want explicit organization                       |
|---------      | like an attribute                 |                                                                 |
|Use Case       | Simple read-only attributes       | When combining with @setter and @deleter                        |
|Equivalent To  | `@radius.getter`                  | @property                                                       |

