import request from '@/utils/request'
/**
 * 登录接口
 */
export const authLoginByAccount = (data) => {
  return request({
    url: '/api/jwt-auth/',
    method: 'post',
    data
  })
}

export const getTasks = (data) => {
  return request({
    url: `/api/api/tasks/?page=${data.page}&page_size=${data.pageSize}&type=${data.type}&state=2`,
    method: 'get'
  })
}

export const getNews = (data) => {
  return request({
    url: `/api/api/news/?page=${data.page}&page_size=${data.pageSize}`,
    method: 'get'
  })
}

export const getNewsDetails = (data) => {
  return request({
    url: `/api/api/news/${data.id}/`,
    method: 'get'
  })
}

export const getTasksType = (data) => {
  return request({
    url: '/api/api/tasks_type/',
    method: 'get'
  })
}

export const getTasksSelfComplete = (data) => {
  return request({
    url: `/api/api/complete_tasks/?page=${data.page}&page_size=${data.pageSize}&state=${data.state}&complete_user=${data.complete_user}`,
    method: 'get'
  })
}

export const sumbitTasks = (data) => {
  return request({
    url: '/api/api/tasks/',
    method: 'post',
    data
  })
}

export const getCode = (data) => {
  return request({
    url: '/api/api/verify/',
    method: 'post',
    data
  })
}

export const register = (data) => {
  return request({
    url: '/api/api/register/',
    method: 'post',
    data
  })
}

export const resetPassword = (data) => {
  return request({
    url: `/api/api/reset_password/${data.username}/`,
    method: 'patch',
    data
  })
}

export const getMoneyRecord = (data) => {
  return request({
    url: `/api/api/money_record/?page=${data.page}&page_size=${data.pageSize}&state=${data.state}&user=${data.user}`,
    method: 'get'
  })
}

export const getCapital = (data) => {
  return request({
    url: `/api/api/capital/?page=${data.page}&page_size=${data.pageSize}&type=${data.type}&user=${data.user}`,
    method: 'get'
  })
}

export const getBanner = (data) => {
  return request({
    url: 'api/api/banner/',
    method: 'get'
  })
}

export const pickTask = (data) => {
  return request({
    url: '/api/api/complete_tasks/',
    method: 'post',
    data
  })
}

export const submitImage = (data) => {
  return request({
    url: '/api/api/image/',
    method: 'post',
    headers: {'Content-Type': 'application/json'},
    data
  })
}

export const homePage = (data) => {
  return request({
    url: '/api/api/homepage/',
    method: 'get'
  })
}


export const grtUser = (data) => {
  return request({
    url: `/api/api/user_balance/?username=${data.user}`,
    method: 'get'
  })
}


export const updatePassword = (data) => {
  return request({
    url: `/api/api/update_password/${data.username}/`,
    method: 'patch',
    data
  })
}


export const updateZFB = (data) => {
  return request({
    url: `/api/api/user/${data.username}/`,
    method: 'patch',
    data
  })
}


export const myTeam = (data) => {
  return request({
    url: `/api/api/team/?page=${data.page}&page_size=${data.pageSize}`,
    method: 'get'
  })
}


export const myTasks = (data) => {
  return request({
    url: `/api/api/my_tasks/?page=${data.page}&page_size=${data.pageSize}`,
    method: 'get'
  })
}


export const deleteMyTasks = (data) => {
  return request({
    url: `/api/api/tasks/${data.tasks_id}/`,
    method: 'patch',
    data
  })
}


export const Transfer = (data) => {
  return request({
    url: '/api/api/transfer/',
    method: 'post',
    data
  })
}
