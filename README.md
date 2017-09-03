# WebSpiderForJob

## Change Log
**v0.13.1(2017/9/2)**
* Add self ip into ip list since self ip is the most stable and quick ip among the ip list. The program can double its process time.
* Fix the bug: can not turn to next page when current page is finish.

**v0.13(2017/9/2)**
* Improve IP storage. Use lock method to lock the ip list so that every time only one thread can call the ip list. It will get one ip from ip list and remove this ip when it is using. If this ip works normally, it will be appended back to the ip list. If this ip fail, it will just throw away. So every thread will have more possibility to use good ip.
* To use set_page_load_timeout method to limit the load time of chrome. It significantly increases the effeciency.
